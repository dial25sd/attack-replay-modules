import argparse

import nmap


def fingerprint(dest_ip, dest_port):
    nm = nmap.PortScanner()

    # Check for IPv6
    use_ipv6 = ':' in dest_ip
    arguments = '-6' if use_ipv6 else ''

    # Perform service scan
    print(f"Starting portscan for {dest_ip}:{dest_port} ...")
    nm.scan(dest_ip, str(dest_port), arguments=f'{arguments} -sV -T4 -Pn')

    # Check if the given port is open
    port_info = nm[dest_ip].get('tcp').get(int(dest_port))

    if port_info and port_info['state'] == 'open':
        print(f"Port {dest_port} is open.")
        print(f"Fingerprint: {port_info['product']} {port_info['version']} {port_info['extrainfo']}")
    else:
        print(f"Port {dest_port} is not open or not found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Service fingerprinting for a given IP addr and port")
    parser.add_argument("destination_ip", help="The IP address to scan")
    parser.add_argument("destination_port", type=int, help="The port number to scan")
    args = parser.parse_args()

    try:
        fingerprint(args.destination_ip, args.destination_port)
    except Exception as e:
        print(f"Fingerprinting Error: {e}")
    finally:
        exit()
