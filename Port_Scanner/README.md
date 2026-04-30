# Port Scanner

A Python-based network reconnaissance tool designed to identify open ports and their associated services on a target host.

## How It Works

This tool is a **TCP Connect Scanner**. It works by attempting to complete the **Three-Way Handshake** that governs how computers establish a reliable connection over a network.

## Logic Breakdown

**Socket Configuration:**
- `AF_INET` — Specifies the use of IPv4 addresses
- `SOCK_STREAM` — Specifies the TCP protocol (connection-oriented)
- `setdefaulttimeout(0.5)` — Sets a 0.5-second limit to prevent hanging on filtered ports

**The Connection Attempt (`connect_ex`):**
- Unlike `connect()`, `connect_ex()` returns an error code instead of raising an exception
- Result `0` — Port is **Open**
- Any other result — Port is **Closed** or **Filtered**

**Service Identification:**
- Uses `getservbyport()` to map port numbers to service names (e.g., Port 80 = HTTP)
- `try/except` block handles unknown services gracefully

## Data Flow & Network Behavior

| Step | Action |
|------|--------|
| Input | User provides target IP address |
| Iteration | Script loops through ports 1-1024 |
| SYN Sent | Connection attempt made to each port |
| SYN-ACK | Port is Open — recorded and closed |
| RST | Port is Closed |
| Timeout | Port is Filtered by firewall |

## Security Context

### Reconnaissance (Offensive View)
This tool maps the **attack surface** of a target:
- **Port 22 (SSH)** — May lead to brute-force attempts
- **Port 80/443 (HTTP/S)** — Signals a web server vulnerable to web attacks

### Mitigation (Defensive View)
- **Firewalls** — Drop unsolicited packets so ports appear Filtered
- **IDS (Intrusion Detection Systems)** — Detect rapid connection attempts and auto-block the source

## Usage

```bash
python3 port_scanner.py
```

## Requirements
- Python 3.x
- No external libraries required