#!/usr/bin/env python3
"""
port_scanner.py — A simple TCP port scanner
Author  : Your Name
GitHub  : github.com/yourhandle
Purpose : Cybersecurity learning project — scans open ports on a target host
"""

import socket
import sys
import argparse
from datetime import datetime


# ─────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────
def print_banner():
    print("""
    ╔══════════════════════════════════════╗
    ║         Simple Port Scanner         ║
    ║      Built for Learning Purposes     ║
    ╚══════════════════════════════════════╝
    """)


# ─────────────────────────────────────────────
# RESOLVE HOSTNAME TO IP
# ─────────────────────────────────────────────
def resolve_host(target):
    """Convert hostname to IP address"""
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"[ERROR] Cannot resolve hostname: {target}")
        sys.exit(1)


# ─────────────────────────────────────────────
# SCAN A SINGLE PORT
# ─────────────────────────────────────────────
def scan_port(ip, port, timeout=1):
    """
    Try to connect to ip:port
    Returns True if port is open, False if closed
    """
    try:
        # Create a new socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Try to connect — returns 0 if successful
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            return True   # Port is OPEN
        else:
            return False  # Port is CLOSED

    except socket.error:
        return False


# ─────────────────────────────────────────────
# GET SERVICE NAME FOR COMMON PORTS
# ─────────────────────────────────────────────
def get_service(port):
    """Return common service name for well-known ports"""
    common_ports = {
        21:   "FTP",
        22:   "SSH",
        23:   "Telnet",
        25:   "SMTP",
        53:   "DNS",
        80:   "HTTP",
        110:  "POP3",
        143:  "IMAP",
        443:  "HTTPS",
        445:  "SMB",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        6379: "Redis",
        8080: "HTTP-Alt",
        8443: "HTTPS-Alt",
        27017:"MongoDB",
    }
    return common_ports.get(port, "Unknown")


# ─────────────────────────────────────────────
# MAIN SCANNER FUNCTION
# ─────────────────────────────────────────────
def run_scanner(target, start_port, end_port, timeout):
    """Main scanning loop"""

    ip = resolve_host(target)

    print_banner()
    print(f"  [*] Target   : {target} ({ip})")
    print(f"  [*] Ports    : {start_port} - {end_port}")
    print(f"  [*] Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 45)

    open_ports = []

    for port in range(start_port, end_port + 1):
        # Show progress every 100 ports
        if port % 100 == 0:
            print(f"  [*] Scanning port {port}...", end="\r")

        if scan_port(ip, port, timeout):
            service = get_service(port)
            open_ports.append(port)
            print(f"  [OPEN]  Port {port:<6} —  {service}")

    # ── Summary ──
    print("-" * 45)
    print(f"  [*] Scan complete at {datetime.now().strftime('%H:%M:%S')}")
    print(f"  [*] Open ports found: {len(open_ports)}")

    if open_ports:
        print(f"  [*] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("  [*] No open ports found in this range.")


# ─────────────────────────────────────────────
# ARGUMENT PARSER — command line interface
# ─────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple Python Port Scanner — Learning Project",
        epilog="Example: python3 port_scanner.py scanme.nmap.org -s 1 -e 1000"
    )
    parser.add_argument(
        "target",
        help="Target IP address or hostname (e.g. 192.168.1.1)"
    )
    parser.add_argument(
        "-s", "--start",
        type=int,
        default=1,
        help="Start port (default: 1)"
    )
    parser.add_argument(
        "-e", "--end",
        type=int,
        default=1024,
        help="End port (default: 1024)"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=float,
        default=1.0,
        help="Timeout per port in seconds (default: 1.0)"
    )
    return parser.parse_args()


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    args = parse_args()

    # Basic validation
    if args.start < 1 or args.end > 65535:
        print("[ERROR] Ports must be between 1 and 65535")
        sys.exit(1)

    if args.start > args.end:
        print("[ERROR] Start port cannot be greater than end port")
        sys.exit(1)

    try:
        run_scanner(args.target, args.start, args.end, args.timeout)
    except KeyboardInterrupt:
        print("\n\n  [!] Scan interrupted by user. Exiting.")
        sys.exit(0)
