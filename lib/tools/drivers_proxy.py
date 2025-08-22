from lib.tools.utils import proxy_info_texts
from lib.tools.colors import red
import requests
import random
import concurrent.futures
import os
import socket

def fetch_proxyscrape_socks5():
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5%22"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()

    proxies = []
    for line in r.text.splitlines():
        line = line.strip()
        if line and ":" in line:
            proxies.append(f"socks5://{line}")
    print(proxy_info_texts["total"].format(total=len(proxies)))
    return proxies


def check_proxy(proxy, timeout=5):
    try:
        ip, port = proxy.replace("socks5://", "").split(":")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, int(port)))
        sock.close()
        return result == 0
    except:
        return False

def save_proxies(filename, proxies):
    short_path = os.path.relpath(filename, os.getcwd())
    print(proxy_info_texts["saving"].format(alive=len(alive_proxies), path=short_path))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for p in proxies:
            f.write(p + "\n")
    print(proxy_info_texts["done"])

def update_proxies():
    all_proxies = fetch_proxyscrape_socks5()
    print(proxy_info_texts["checking"])
    alive_proxies = [p for p in all_proxies if check_proxy(p)]
    print(proxy_info_texts["alive"].format(alive=len(alive_proxies)))
    output_path = os.path.join(os.path.dirname(__file__), "../files/proxy.txt")
    save_proxies(output_path, alive_proxies)
    return alive_proxies
