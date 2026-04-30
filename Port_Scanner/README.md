Port Scanner
A Python-based network reconnaissance tool designed to identify open ports and their associated services on a target host.

How It Works
This tool is a TCP Connect Scanner. It works by attempting to complete the "Three-Way Handshake" that governs how computers establish a reliable connection over a network.

The Logic Breakdown
Socket Configuration:


AF_INET: Specifies the use of IPv4 addresses.


SOCK_STREAM: Specifies the TCP protocol, which is connection-oriented.


setdefaulttimeout(0.5): Sets a 0.5-second limit for responses to prevent the script from hanging on non-responsive (filtered) ports.

The Connection Attempt (connect_ex):

Unlike a standard connect() call, connect_ex() returns an error code instead of raising an exception.


Result 0: Indicates a successful connection—the port is Open.


Any other result: Indicates the port is Closed or Filtered.

Service Identification:

The tool uses getservbyport() to look up the standard service name associated with the port number (e.g., Port 80 is HTTP).

A try/except block handles "Unknown Services" to ensure the script doesn't crash on obscure ports.

Data Flow & Network Behavior

Input: The user provides a target IP address.


Iteration: The script loops through port numbers 1 to 1024.


The Request: For each port, a SYN (Synchronize) packet is sent to the target.

The Response:

Open Port: The target sends a SYN-ACK. The script records success and closes the connection.


Closed Port: The target sends an RST (Reset).


Filtered: A firewall drops the packet; the script hits its timeout and moves on.


Output: The results are printed to the console, mapping open ports to their known services.

Security Context
Reconnaissance (Offensive View)
In the security world, this is the Reconnaissance phase. An attacker uses this to map the "attack surface" of a target. For example:


Port 22 (SSH): Might lead to brute-force attempts.


Port 80/443 (HTTP/S): Signals a web server to test for web vulnerabilities.

Mitigation (Defensive View)
Security professionals defend against port scanning by:


Firewalls: Configured to drop unsolicited packets so ports appear "Filtered".


Intrusion Detection Systems (IDS): These systems can detect rapid connection attempts from a single IP and automatically block the source.