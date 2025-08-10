import time, csv, os, argparse, statistics, subprocess, platform, re

def read_signal_windows(target_ssid):
    out = subprocess.check_output(['netsh','wlan','show','interfaces'], text=True, errors='ignore')
    ssid_m = re.search(r'SSID\s+:\s+(.+)', out)
    sig_m = re.search(r'Signal\s+:\s+(\d+)%', out)
    return (ssid_m.group(1).strip() if ssid_m else None,
            int(sig_m.group(1)) if sig_m else None)

def read_signal_linux(target_ssid):
    out = subprocess.check_output(['nmcli','-t','-f','active,ssid,signal','dev','wifi'], text=True, errors='ignore')
    for line in out.splitlines():
        active, ssid, sig = (line.split(':')+['',''])[:3]
        if active=='yes':
            return ssid, int(sig) if sig else None
    return None, None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--interval', type=int, default=5)
    ap.add_argument('--duration', type=int, default=60)
    ap.add_argument('--out', default='reports/signal_log.csv')
    ap.add_argument('--ssid', default=None)
    args = ap.parse_args()

    os.makedirs('reports', exist_ok=True)
    end = time.time()+args.duration
    rows = []
    while time.time()<end:
        if 'windows' in platform.system().lower():
            ssid, sig = read_signal_windows(args.ssid)
        else:
            ssid, sig = read_signal_linux(args.ssid)
        ts = int(time.time())
        rows.append([ts, ssid or '', sig or -1])
        print(ts, ssid, sig)
        time.sleep(args.interval)

    import csv
    with open(args.out,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['ts','ssid','signal_pct'])
        w.writerows(rows)
    print(f'Saved {len(rows)} samples to {args.out}')

if __name__ == '__main__':
    main()
