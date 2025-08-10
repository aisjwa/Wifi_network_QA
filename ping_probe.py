import argparse, subprocess, sys, statistics

def ping(host='8.8.8.8', count=10):
    cmd = ['ping','-n' if sys.platform=='win32' else '-c', str(count), host]
    out = subprocess.check_output(cmd, text=True, errors='ignore')
    times = []
    for tok in out.replace('=',' ').split():
        if tok.endswith('ms'):
            try: times.append(float(tok[:-2]))
            except: pass
    if times:
        print(f'avg={statistics.mean(times):.1f}ms p95={statistics.quantiles(times, n=20)[-1]:.1f}ms')
    else:
        print('No RTTs parsed.')

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--host', default='8.8.8.8')
    ap.add_argument('--count', type=int, default=10)
    args = ap.parse_args()
    ping(args.host, args.count)
