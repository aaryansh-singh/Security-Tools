# Packet Sniffer

A Python-based network traffic analysis tool built with the Scapy library to capture and inspect real-time data packets. This tool demonstrates how to intercept network traffic and extract critical header information from the IP and Transport layers.

## How It Works

This tool performs **Passive Sniffing**, acting as a digital wiretap that monitors data as it flows through your network interface. By analyzing packet headers, it identifies the source, destination, and protocols used — without disrupting network traffic.

## Logic Breakdown

**The `sniff()` Engine:**
- `Capture` — Intercepts raw packets directly from the network interface
- `prn=analyze_packet` — A callback function that processes every captured packet in real-time
- `count=20` — Limits the session to 20 packets to keep output focused and manageable

**Protocol Dissection:**
- `IP Layer` — Extracts Source IP and Destination IP to identify communication endpoints
- `Transport Layer (TCP/UDP)` — Identifies specific port numbers and traffic types
- `Error Handling` — Catch-all for non-TCP/UDP packets (ICMP/Ping) to ensure no data is missed

## Data Flow

| Step | Action |
|------|--------|
| Initialization | Script starts the Scapy sniff engine |
| Capture | Network card intercepts a raw packet |
| Peeling (IP) | Script extracts source and destination addresses |
| Peeling (Transport) | Script identifies TCP/UDP ports and service types |
| Output | Formatted summary printed to console |

## Security Context

### Traffic Analysis (Offensive View)
Sniffing is a critical component of network reconnaissance:
- **Credential Harvesting** — Unencrypted traffic (HTTP, FTP) can reveal plain-text passwords
- **Network Mapping** — Silently map active devices without sending loud scan packets

### Monitoring & Defense (Defensive View)
- **Incident Response** — Identify compromised machines by spotting connections to malicious IPs
- **Troubleshooting** — Verify if firewalls are correctly allowing or blocking specific traffic

## Usage

> **Note:** Root or Administrative privileges are required to capture raw network packets.

```bash
sudo python3 packet_sniffer.py
```

## Requirements

- Python 3.x
- Scapy Library
