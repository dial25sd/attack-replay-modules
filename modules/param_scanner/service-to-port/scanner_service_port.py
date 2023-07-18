import argparse
import re

import nmap


def scan(target, regex):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sV -T4')
    found = False

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = list(nm[host][proto].keys())
            ports.sort()
            for port in ports:
                port_info = nm[host][proto][port]
                match = re.search(regex, port_info['product'])
                if match and port_info['state'] == 'open':
                    found = True
                    print(f"Matching service detected on port: {port}")
    if not found:
        print(f"No match found for service name '{regex}'.")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description='Param scanner to find the port number used by a service whose name matches the given regex')
        parser.add_argument('target', help='Target IP addr or hostname')
        parser.add_argument('regex', help='Regex to match in the service name')
        args = parser.parse_args()

        scan(args.target, args.regex)
    except Exception as e:
        exit(e)
