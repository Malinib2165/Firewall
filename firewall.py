import socket

# Blocked IPs and ports
BLOCKED_IPS = {"192.168.1.100", "10.0.0.5"}
BLOCKED_PORTS = {23, 445}

def check_traffic(ip, port, direction):
    if ip in BLOCKED_IPS:
        return f"[BLOCKED] {direction} traffic from/to IP: {ip}"

    if port in BLOCKED_PORTS:
        return f"[BLOCKED] {direction} traffic on port: {port}"

    return f"[ALLOWED] {direction} traffic from/to {ip}:{port}"

def main():
    print("=== Simple Python Firewall ===")

    while True:
        ip = input("Enter IP address (or 'exit'): ")
        if ip.lower() == "exit":
            break

        port = int(input("Enter port: "))
        direction = input("Direction (incoming/outgoing): ")

        result = check_traffic(ip, port, direction)
        print(result)
        print("-" * 40)

if __name__ == "__main__":
    main()
