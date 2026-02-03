import socket

target = input("Enter target IP address: ")

# Common ports
ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP"
}

print(f"\nScanning target: {target}\n")

for port, service in ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} OPEN ({service})")
    else:
        print(f"[-] Port {port} CLOSED")

    sock.close()
