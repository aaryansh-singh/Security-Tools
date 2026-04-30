# Log Analyzer

A Python-based threat detection tool that scans system authentication logs for multiple suspicious activity patterns simultaneously.

## How It Works

Unlike a single-purpose detector, this tool performs **Multi-Pattern Log Analysis** — scanning for several threat types in a single pass and generating a consolidated security report.

## Logic Breakdown

**Pattern Dictionary:**
- Defines multiple threat signatures in one place
- Easy to extend — add new threats by adding one line
- Current patterns: Brute Force, Root Access, Invalid User

**Smart IP Extraction:**
- Uses `parts.index("from") + 1` to find the IP regardless of log format
- `try/except` handles malformed lines gracefully

**Aggregation & Reporting:**
- `defaultdict(list)` stores every IP per threat type
- `set(ips)` deduplicates — shows unique attackers
- `ips.count(ip)` shows how many times each attacker struck

## Data Flow

| Step | Action |
|------|--------|
| Ingestion | Opens auth.log for reading |
| Pattern Matching | Each line checked against all threat signatures |
| Extraction | Source IP extracted using "from" keyword |
| Aggregation | IPs grouped by threat type |
| Reporting | Consolidated threat report printed to console |

## Security Context

### Offensive View
- **Reconnaissance** — Attackers probe with multiple techniques simultaneously
- **Privilege Escalation** — Root login attempts signal intent to gain full system control

### Defensive View
- **SIEM Systems** — Enterprise tools like Splunk use this exact multi-pattern logic at massive scale
- **Threat Correlation** — Same IP appearing in multiple threat categories = high priority target

## Usage

```bash
python3 log_analyzer.py
```

## Requirements

- Python 3.x
- Standard Library only