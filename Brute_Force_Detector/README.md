# Brute Force Detector

A Python-based log analysis tool designed to detect potential brute-force attacks by monitoring failed login attempts within system authentication logs.

## How It Works

This tool performs **Automated Log Parsing**. It scans system security files (like `auth.log`) to identify patterns of repeated authentication failures originating from the same source IP address.

## Logic Breakdown

**Log Monitoring & Thresholds:**
- `THRESHOLD = 5` — If an IP fails to login more than 5 times, it is flagged as a threat
- `defaultdict(int)` — Automatically initializes a count of 0 for any new IP encountered

**Pattern Matching:**
- `if "Failed password" in line` — Searches for strings used by SSH to record login failures
- `Line Splitting` — Extracts the 6th element (index 5), which is the Source IP address

**Alerting Mechanism:**
- `if count >= THRESHOLD` — Compares total failures per IP against the security policy and prints an ALERT

## Data Flow

| Step | Action |
|------|--------|
| Ingestion | Tool opens auth.log for reading |
| Parsing | Script reads line-by-line to find failure patterns |
| Extraction | Attacker's IP is extracted from the log entry |
| Aggregation | Failure count for that IP is updated in memory |
| Detection | Script checks which IPs exceeded the threshold |
| Reporting | Summary of suspicious IPs printed to console |

## Security Context

### Brute Force Attacks (Offensive View)
- **Credential Stuffing** — Using leaked passwords from other breaches
- **Dictionary Attacks** — Testing common passwords like "password123"

### Intrusion Detection (Defensive View)
- **Automated Blocking** — Tools like Fail2Ban use this exact logic to update firewall rules
- **Log Auditing** — Identifies which accounts are being targeted most frequently

## Usage

> **Note:** Accessing system logs like `/var/log/auth.log` requires root privileges.

```bash
sudo python3 brute_force_detector.py
```

## Requirements

- Python 3.x
- Standard Library (no external installations required)