# Wi‑Fi Network QA – Pro Template

Public‑safe toolkit showing how to validate Wi‑Fi connectivity, stability, and performance for IoT/embedded devices.
Designed to reflect ~4 years QA experience (structured plans, KPIs, automation, CI).

> All SSIDs, MACs, and endpoints are **dummy**. Replace via env vars or `.env` (not committed).

## Highlights
- Cross‑platform scans (Windows `netsh`, Linux `nmcli`) with normalized output
- RSSI/SNR logging over time with CSV + plots
- Latency/packet‑loss checks (ping)
- Throughput sampling using `speedtest-cli` (optional) or iperf placeholder
- Pytest automation + GitHub Actions CI example
- Test plan, KPI sheet, and sample test matrix

## Quick start
```bash
pip install -r requirements.txt
python scripts/scan_wifi.py --once
python scripts/log_signal.py --interval 5 --duration 60
pytest -q
```

## Structure
```
docs/TEST_PLAN.md        # goals, scope, KPIs
docs/MATRIX.md           # channels/bands/auth combinations
scripts/scan_wifi.py     # get AP list (netsh/nmcli) -> CSV
scripts/log_signal.py    # track RSSI for a target SSID/BSSID
scripts/ping_probe.py    # latency/packet loss
scripts/throughput.py    # optional speedtest wrapper (safe)
tests/test_schema.py     # sanity on CSV columns
.github/workflows/pytest.yml  # sample CI
```

