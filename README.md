# Cybersecurity Tools

Python security tools and scripts built while learning cybersecurity.

## 🛠️ Tools

### Port Scanner
A simple TCP port scanner that checks for open ports on a target host.

**Usage:**

python3 port_scanner.py <target> -s <start_port> -e <end_port>

**Example:**

python3 port_scanner.py scanme.nmap.org -s 1 -e 1000

**Arguments:**
| Flag | Description | Default |
|------|-------------|---------|
| `target` | IP address or hostname to scan | required |
| `-s` `--start` | Start port | 1 |
| `-e` `--end` | End port | 1024 |
| `-t` `--timeout` | Timeout per port (seconds) | 1.0 |

**Features:**
- Hostname to IP resolution
- Custom port range scanning
- Common service identification (SSH, HTTP, FTP, etc.)
- Adjustable connection timeout
- Clean CLI output with scan summary

## 🧰 Tech Stack
- Python 3
- Built-in `socket` module
- `argparse` for CLI handling

## 👤 About Me
2nd-year Cybersecurity student, building practical security tools while learning offensive security and Python scripting.

## ⚠️ Disclaimer
These tools are for educational purposes only. Only use on systems you own or have explicit written permission to test. Unauthorized scanning of networks you don't own is illegal.
