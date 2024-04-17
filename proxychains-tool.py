import requests
import argparse

def chain_proxies(proxies, target_url):
    for proxy in proxies:
        try:
            response = requests.get(target_url, proxies={'http': proxy, 'https': proxy}, timeout=10)
            print(f"Proxy: {proxy}, Status Code: {response.status_code}, Response: {response.text}")
        except requests.RequestException as e:
            print(f"Proxy: {proxy}, Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ProxyChains-like tool in Python')
    parser.add_argument('--proxies', nargs='+', help='List of proxy servers (IP:Port)', required=True)
    parser.add_argument('--target', help='Target URL to test proxy chaining', required=True)
    args = parser.parse_args()

    chain_proxies(args.proxies, args.target)
