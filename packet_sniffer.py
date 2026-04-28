from scapy.all import sniff, IP, TCP, UDP

def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            print(f"TCP | {src} -> {dst} | Port {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP | {src} -> {dst} | Port {packet[UDP].sport} -> {packet[UDP].dport}")
        else:
            print(f"OTHER | {src} -> {dst} | Protocol: {protocol}")

print("Sniffing packets... Press Ctrl+C to stop\n")
sniff(prn=analyze_packet, count=20)
