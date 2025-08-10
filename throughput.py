import subprocess, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cli', default='speedtest')  # requires speedtest-cli
    args = ap.parse_args()
    try:
        out = subprocess.check_output([args.cli, '--simple'], text=True, errors='ignore')
        print(out)
    except Exception as e:
        print('Speedtest CLI not available. Document iperf or router-based tests instead.')

if __name__=='__main__':
    main()
