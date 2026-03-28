# Python_PortScanner
Simple Port Scanner utlizing Python as a practice project. WIll improve

## What does it feature?
- Scan target host for open ports in a given range
- Label open ports with their known service names
- Use threading for fast concurrent scanning
- Utilized banner grabs in which service is running at the stated port.

## Usage
python scanner.py --host scanme.nmap.org --ports 1-1024 --timeout 2  

Note: You can change the --host, --ports, and --timeout.

## Test purposes
host = "scanme.nmap.org"  

host = "127.0.0.1"

## Lessons learned
- TCP socket connections and how they work
- Three-way handshake and why it matters
- Threading speeds up network-bound tasks
- Banner Grabbing used to indicate security concerns