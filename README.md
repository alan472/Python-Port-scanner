# Python Port Scanner

A simple Python-based port scanner built to understand network reconnaissance and how open ports expose services on a host.

## Cybersecurity Relevance

Port scanning is one of the first steps in penetration testing and cyber attacks. By identifying open ports, an attacker or security professional can determine which services are running and potentially vulnerable.

This project helped me understand:
- How TCP ports work
- How services listen for connections
- How open ports increase attack surface
- The fundamentals behind tools like Nmap

## Features

- Scans common ports (21, 22, 80, 443, 3389, etc.)
- Identifies open vs closed ports
- Uses TCP socket connections

## How It Works

The script attempts to establish a TCP connection to each port on a target IP address.  
If the connection succeeds, the port is open.  
If it fails or times out, the port is closed.

## How to Run

python3 port_scanner.py

## Example Output

[+] Port 22 OPEN (SSH)  
[-] Port 23 CLOSED  
