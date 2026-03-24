# PYTHON GENERIC PORT SCANNER
# Goal:
# 1. Learn the fundamentals of socket programming in Python
# 2. Create a simple port scanner that can check for open ports on a target host
# 3. Understand how to handle exceptions and errors in Python

# import modules and libraries in Python
from concurrent.futures import ThreadPoolExecutor
import argparse
import socket

#  Add ports and label them in a dict
ports = {
    21: "ftp", # Field Transfer Protocol
    22: "ssh", # Secure Shell
    23: "telnet", # Telnet protocol
    25: "smtp", # Simple Mail Transfer Protocol
    53: "dns", # Domain Name Server
    80: "http", # Hypertext Transfer Protocol
    110: "pop3", # Post Office Protocol
    119: "nntp", # Network News Transfer Protocol
    143: "imap", # Internet Message Access Protocol
    443: "https", # Secure Hypertext Transfer Protocol
    993: "imaps", # Internet Message Access Protocol Secure
    995: "pop3s", # Post Office Protocol Secure
    3306: "mysql", # MySQL
    5432: "postgresql", # PostgreSQL
    6379: "redis", # Redis
    27017: "mongodb", # MongoDB
    # You can add more ports and services as needed for your scanning purposes.
}

# Create a function to perform port scanning. It will allow parameters host & port range
def scan(host,port, timeout=1.0):
    sock = socket.socket()
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# legal host to test against. These are open ports useful for learning and testing purposes.

# Adds command-line arguments for host and port range. This allows users to specify the target host and the range of ports to scan when running the script. 
# The default port range is set to 1-1024, which includes common well-known ports.
parser = argparse.ArgumentParser(description="Port Scanner")

# --host: specifies the target host to scan. required: makes the argument True. help: provides a description of the argument for users when they use the --help option.
parser.add_argument("--host", required=True, help="Target host to scan")

# --ports: specify range of ports to scan. default: sets the default value to "1-1024".
parser.add_argument("--ports", default="1-1024", help="Port range e.g. 1-1024")

# --timeout: specify the timeout for socket connections. default: sets the default value to 1.0 seconds. type: ensures that the input is treated as a float.
parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds for socket connection")

# assign the overall argument to var args
args = parser.parse_args()

# host = "scanme.nmap.org"
# host = "127.0.0.1" # your local machine. Uncomment to test
host = args.host

start, end = args.ports.split("-")
start, end = int(start), int(end)

# print(args.host) # test the host argument. Uncomment to test


# Function to print open ports and their corresponding services.
def scan_print(port):
    if scan(host, port) is True:
        service = ports.get(port, "Unknown")
        print(f"Port {port} has '{service}' open.")

# Add threading to speed up the scanning process
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_print, range(start, end + 1))

# If port is open, check if it's in the map and display service name through a services database.