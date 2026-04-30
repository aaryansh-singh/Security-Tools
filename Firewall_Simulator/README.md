# Firewall Rule Simulator

A Python-based tool that simulates how a firewall evaluates network packets against a defined ruleset to ALLOW or BLOCK traffic.

## How It Works

Implements a **First-Match Rule Engine** — the same logic used in real firewalls like iptables and AWS Security Groups. Rules are evaluated top-to-bottom and the first match wins.

## Logic Breakdown

**Rule Structure:**
- `ip` — Source IP to match (`*` = any IP)
- `port` — Destination port to match (`*` = any port)
- `action` — ALLOW or BLOCK

**Matching Engine:**
- Checks each rule in order until a match is found
- Supports wildcard `*` for both IP and port
- Default action is BLOCK if no rule matches

**Rule Priority:**
- Specific rules placed first take priority over wildcard rules
- Last rule `* -> *` acts as the default policy

## Data Flow

| Step | Action |
|------|--------|
| Packet Arrives | Source IP and destination port extracted |
| Rule Evaluation | Each rule checked top-to-bottom |
| First Match | Action from matching rule is applied |
| Default | BLOCK if no rule matches |
| Output | Decision printed to console |

## Current Ruleset

| IP | Port | Action |
|----|------|--------|
| 192.168.1.10 | 22 | BLOCK |
| 10.0.0.5 | 80 | ALLOW |
| * | 23 | BLOCK |
| * | * | ALLOW |

## Security Context

### Offensive View
- **Firewall Evasion** — Attackers probe for misconfigured rules or use allowed ports to tunnel malicious traffic

### Defensive View
- **Principle of Least Privilege** — Only explicitly needed traffic should be allowed
- **Default Deny** — Change the last rule to BLOCK for a more secure posture

## Usage

```bash
python3 firewall.py
```

## Requirements
- Python 3.x
- Standard Library only