import socket 

target= input("Enter Target IP: ")
print(f"\nScanning {target}... \n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target,port))
    if result == 0:
       try:
           service = socket.getservbyport(port, 'tcp')
       except OSError:
           service = "Unknown Service"
       
       print(f"Port {port} is OPEN - Service: {service}")
       print(f"Port {port} is OPEN")
    s.close()

print("\nScan complete")
