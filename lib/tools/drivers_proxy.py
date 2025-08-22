import requests
from bs4 import BeautifulSoup
import random
import os
import socket

PROXY_FILE = os.path.join(os.path.dirname(__file__), "..", "files", "proxy.txt")

def fetch_socks5_proxies():
    // Ambil proxy SOCKS5 dari website publik
    proxies = []
    try:
        r = requests.get("https://www.socks-proxy.net/", timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        if not table:
            return []

        for row in table.tbody.find_all("tr"):
            tds = row.find_all("td")
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxy_type = tds[4].text.strip()
            if proxy_type.upper() == "SOCKS5":
                proxies.append(f"socks5://{ip}:{port}")
    except:
        pass
    return proxies

def check_proxy_alive(proxy, timeout=5):
    """Cek apakah proxy bisa connect"""
    try:
        ip_port = proxy.replace("socks5://", "").split(":")
        ip, port = ip_port[0], int(ip_port[1])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

def update_alive_proxies():
    """Ambil proxy, cek alive, simpan ke proxy.txt"""
    proxies = fetch_socks5_proxies()
    alive_proxies = [p for p in proxies if check_proxy_alive(p)]
    # simpan ke file
    with open(PROXY_FILE, "w") as f:
        for p in alive_proxies:
            f.write(p + "\n")
    return alive_proxies

def get_random_proxy():
    """Ambil random proxy dari proxy.txt, update jika kosong"""
    if not os.path.exists(PROXY_FILE) or os.path.getsize(PROXY_FILE) == 0:
        update_alive_proxies()

    with open(PROXY_FILE, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    if not proxies:
        return None
    return random.choice(proxies)
    