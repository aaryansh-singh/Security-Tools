from collections import defaultdict

THRESHOLD = 5
failed_attempts = defaultdict(int)

with open("auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[5]
            failed_attempts[ip] += 1

print("Brute Force Detection Report")
print("=" * 40)
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"ALERT: {ip} — {count} failed attempts")
