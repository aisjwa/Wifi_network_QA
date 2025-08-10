# Wi‑Fi QA Test Plan (Generic)

## Scope
- Association, DHCP, DNS resolution
- Authentication: Open, WPA2‑PSK, WPA3‑SAE (conceptual)
- Bands: 2.4 GHz / 5 GHz; Channels: 1/6/11, 36/44/149
- Metrics: RSSI, SNR, latency, jitter, packet loss, throughput

## KPIs (example)
- Assoc success rate ≥ 99%
- DHCP success ≥ 99.5%
- Median RSSI at test point ≥ −65 dBm
- P95 ping latency ≤ 50 ms; packet loss < 1%
- Downlink throughput (best‑effort) ≥ 30 Mbps (lab router)

## Procedure
1) Scan & select target SSID/BSSID.
2) Connect (manual step for demo) and verify IP + internet reachability.
3) Run `log_signal.py` for 5–10 minutes.
4) Run `ping_probe.py` to a public target (8.8.8.8) or local router.
5) (Optional) Run `throughput.py` for a quick estimate.
