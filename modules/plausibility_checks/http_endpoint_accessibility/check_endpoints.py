import argparse
import ipaddress
import requests
from requests.exceptions import RequestException, Timeout


def check_url(protocol, host, port, endpoint, method, timeout):
    # check if IP address is IPv6 or IPv6
    try:
        ip = ipaddress.ip_address(host)
        if ip.version == 6 and not host.startswith('['):
            host = f"[{host}]"
    except ValueError:
        pass

    url = f"{protocol}://{host}:{port}"
    complete_url = f"{url}{endpoint}" if endpoint.startswith('/') else f"{url}/{endpoint}"
    try:
        response = requests.request(method, complete_url, timeout=timeout)
        print(f"Got HTTP {response.status_code} for '{endpoint}'")
        if 200 <= response.status_code < 400:
            return True, complete_url
    except (RequestException, Timeout) as e:
        print(f"Got error {e} for '{endpoint}'")
        pass
    return False, complete_url


def main():
    parser = argparse.ArgumentParser(description="Check the accessibility of given HTTP endpoints")
    parser.add_argument("protocol", help="Protocol of the target service")
    parser.add_argument("host", help="Hostname or IP addr of the target system")
    parser.add_argument("port", type=int, help="Port of the target service")
    parser.add_argument("method", choices=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
                        help="The HTTP method to use for the requests")
    parser.add_argument("timeout", type=int, default=60, help="Timeout for a single request in seconds. Defaults to 5)")
    parser.add_argument("endpoints", nargs="+", help="A list of endpoints to check. Can be separated by a whitespace")

    args = parser.parse_args()
    found_endpoint = False

    individual_timeout = int((args.timeout - 5) / len(args.endpoints)) if args.timeout > 5 else 0
    for endpoint in list(set(args.endpoints)):
        is_reachable, url = check_url(args.protocol, args.host, args.port, endpoint, args.method, individual_timeout)
        if is_reachable:
            print(f"Endpoint is reachable: {url}")
            found_endpoint = True

    if not found_endpoint:
        print("No reachable endpoint found.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        exit(e)
