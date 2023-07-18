import argparse
import socket
from contextlib import closing


def get_address_info(dest_ip):
    try:
        for response in socket.getaddrinfo(dest_ip, None):
            family, _, _, _, _ = response
            if family == socket.AF_INET:
                return socket.AF_INET
            elif family == socket.AF_INET6:
                return socket.AF_INET6
    except socket.gaierror:
        print("Invalid IP address.")
        exit(1)


def is_port_open(dest_ip, dest_port, timeout):
    family = get_address_info(dest_ip)  # Determine if the address is an IPv4 or IPv6 address
    with closing(socket.socket(family, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((dest_ip, dest_port))
        return result == 0  # 0 means the connection was successful (port is open)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Check if a port is open on a host.")
        parser.add_argument("destination_ip", help="The IP address to check.")
        parser.add_argument("destination_port", type=int, help="The port number to check.")
        parser.add_argument("timeout", type=int, default=30, help="Timeout for the connection attempt in seconds.")
        args = parser.parse_args()

        if is_port_open(args.destination_ip, args.destination_port, args.timeout):
            print(f"Port is open on host: {args.destination_ip}:{args.destination_port}.")
        else:
            print("Port does not seem to be open.")
    except Exception as e:
        exit(e)
