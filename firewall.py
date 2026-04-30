rules = [
    {"ip": "192.168.1.10", "port": 22, "action": "BLOCK"},
    {"ip": "10.0.0.5", "port": 80, "action": "ALLOW"},
    {"ip": "*", "port": 23, "action": "BLOCK"},
    {"ip": "*", "port": "*", "action": "ALLOW"},
]

def check_packet(src_ip, dst_port):
    for rule in rules:
        ip_match = rule["ip"] == src_ip or rule["ip"] == "*"
        port_match = rule["port"] == dst_port or rule["port"] == "*"
        if ip_match and port_match:
            return rule["action"]
    return "BLOCK"

packets = [
    ("192.168.1.10", 22),
    ("10.0.0.5", 80),
    ("172.16.0.1", 23),
    ("8.8.8.8", 443),
]

print("Firewall Simulation Report")
print("=" * 40)
for ip, port in packets:
    result = check_packet(ip, port)
    print(f"{result} | {ip} -> Port {port}")
