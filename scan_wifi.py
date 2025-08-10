import csv, subprocess, sys, platform, re, argparse, pandas as pd

def scan_windows():
    out = subprocess.check_output(['netsh','wlan','show','networks','mode=Bssid'], text=True, errors='ignore')
    blocks = out.split('\n\n')
    rows = []
    for b in blocks:
        ssid_m = re.search(r'SSID \d+ : (.+)', b)
        if not ssid_m: continue
        ssid = ssid_m.group(1).strip()
        for bssid, sig, chan in re.findall(r'BSSID \d+ : ([\w:]+).*?Signal : (\d+)%.*?Channel : (\d+)', b, re.S):
            rows.append({'ssid': ssid, 'bssid': bssid, 'signal_pct': int(sig), 'channel': int(chan), 'band': '2.4/5?'})

    return rows

def scan_linux():
    out = subprocess.check_output(['nmcli','-f','SSID,BSSID,CHAN,SIGNAL','dev','wifi'], text=True, errors='ignore')
    rows = []
    for line in out.splitlines()[1:]:
        parts = [p.strip() for p in line.split()]
        if len(parts) < 4: continue
        ssid = parts[0]
        bssid = parts[1]
        chan = int(parts[2]) if parts[2].isdigit() else None
        sig = int(parts[3]) if parts[3].isdigit() else None
        rows.append({'ssid': ssid, 'bssid': bssid, 'signal_pct': sig, 'channel': chan, 'band': '2.4/5?'})
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='reports/scan.csv')
    ap.add_argument('--once', action='store_true')
    args = ap.parse_args()
    osname = platform.system().lower()
    rows = scan_windows() if 'windows' in osname else scan_linux()
    import os; os.makedirs('reports', exist_ok=True)
    pd.DataFrame(rows).to_csv(args.out, index=False)
    print(f'Saved {len(rows)} entries to {args.out}')

if __name__ == '__main__':
    main()
