import os
import json
import random
import re
import requests

# Hardcoded fallback User-Agents
FALLBACK_UA = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
]

USER_AGENT_FILE = os.path.join(os.path.dirname(__file__), "../files/user_agent.txt")
BROWSERS = ["chrome", "edge", "safari", "firefox", "firefox-esr"]
BLACKLIST_KEYWORDS = [
    "sleep", "timeout", "get-help", "start", "system", "Functionize",
    "assetnote", "gzip", "norton", "avast", "ccleaner", "avg"
]

def fetch_user_agents(api_key: str, limit=100):
    """Fetch User-Agents from WhatIsMyBrowser API"""
    agents = []
    headers = {"X-API-KEY": api_key}
    for browser in BROWSERS:
        url = f"https://api.whatismybrowser.com/api/v2/user_agent_database_search?order_by=times_seen%20desc&hardware_type=computer&limit={limit}&software_name={browser}"
        try:
            r = requests.get(url, headers=headers, timeout=10, verify=False)
            r.raise_for_status()
            data = r.json()
            results = data.get("search_results", {}).get("user_agents", [])
            for ua in results:
                ua_string = ua.get("user_agent", "")
                if not any(k.lower() in ua_string.lower() for k in BLACKLIST_KEYWORDS) and not re.search(r"\(?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\)?$", ua_string):
                    agents.append(ua_string)
        except Exception:
            continue
    return agents or FALLBACK_UA

def save_user_agents(agents, path=USER_AGENT_FILE, count=100):
    """Save random sample of user agents to file"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for _ in range(count):
            f.write(random.choice(agents) + "\n")
    print(f"[INFO] Saved {count} user-agents to {path}")

def update_user_agents():
    """Update User-Agent file"""
    api_key = os.getenv("WHATISMYBROWSER_KEY")
    if api_key:
        agents = fetch_user_agents(api_key)
    else:
        agents = FALLBACK_UA
    save_user_agents(agents)
    return USER_AGENT_FILE

def get_random_user_agent(filepath=None):
    """Get one random user-agent from file"""
    if filepath is None:
        filepath = USER_AGENT_FILE
    if not os.path.exists(filepath):
        update_user_agents()
    with open(filepath, "r") as f:
        agents = [line.strip() for line in f if line.strip()]
    return random.choice(agents) if agents else random.choice(FALLBACK_UA)
