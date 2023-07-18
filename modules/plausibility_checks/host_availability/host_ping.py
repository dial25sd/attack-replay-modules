import argparse

from icmplib import ping


def check_connectivity(dest_ip, timeout):
    try:
        host = ping(dest_ip, count=5, interval=0.6, timeout=timeout/5)
        if host.is_alive:
            print(f"Successfully reached IP {dest_ip}.")
        else:
            print("Failed to reach IP.")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Ping a given IP addr")
        parser.add_argument("ip", help="The IP address to ping")
        parser.add_argument("timeout", type=int, default=4, help="Timeout for the ping command in seconds")
        args = parser.parse_args()

        check_connectivity(args.ip, args.timeout)
    except Exception as e:
        exit(e)
