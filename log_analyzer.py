from collections import defaultdict

suspicious = defaultdict(list)

patterns = {
    "Brute Force": "Failed password",
    "Root Access": "root login",
    "Invalid User": "Invalid user"
}

with open("auth.log", "r") as f:
    for line in f:
        for threat, pattern in patterns.items():
            if pattern in line:
                parts = line.split()
                try:
                    idx = parts.index("from") + 1
                    ip = parts[idx]
                except (ValueError, IndexError):
                    ip = "unknown"
                suspicious[threat].append(ip)

print("Log Analysis Report")
print("=" * 40)
for threat, ips in suspicious.items():
    print(f"\n[{threat}] — {len(ips)} incidents detected")
    for ip in set(ips):
        print(f"  -> {ip} ({ips.count(ip)} times)")
