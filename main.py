from lib.tools.drivers_proxy import update_proxies
from lib.tools.drivers_user_agent import update_user_agents, get_random_user_agent
from lib.tools.utils import green_text, red_texts, info_text, banner, proxy_info_texts
from lib.tools.colors import red, green, white, reset
import time
import random
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def log_result(status, url, proxy, ua):
    base_path = os.path.join(os.path.dirname(__file__), "lib", "files")
    os.makedirs(base_path, exist_ok=True)

    if status == "done":
        file_path = os.path.join(base_path, "result_done.txt")
    else:
        file_path = os.path.join(base_path, "result_fail.txt")

    with open(file_path, "a") as f:
        f.write(f"{url} | Proxy: {proxy} | UA: {ua}\n")

def Coba_GueLiat_Dulu(file_name):
    base_path = os.path.join(os.path.dirname(__file__), "lib", "data")
    full_path = os.path.join(base_path, file_name)
    with open(full_path, "r") as f:
        data = json.load(f)
    return data

def random_delay(min_delay=0.5, max_delay=2):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

def get_random_proxy(filepath="lib/files/proxy.txt"):
    with open(filepath, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    return random.choice(proxies) if proxies else None


def init_driver(proxy=None, user_agent=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-webgl")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--silent")
    options.add_argument("--disable-ffmpeg")
    options.add_argument("--disable-logging")

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    if user_agent:
        options.add_argument(f'--user-agent={user_agent}')        
    return webdriver.Chrome(options=options)
    driver.set_page_load_timeout(100)
    return driver

def find_element_by_multiple_attributes(driver, tag_name, attributes):
    for attribute in attributes:
        try:
            return WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"{tag_name}[{attribute}]"))
            )
        except TimeoutException:
            continue
    return None

def dofollow(urls, Koleksi_Bacotan):
    Tumpukan_Bacotan = Coba_GueLiat_Dulu(Koleksi_Bacotan)

    for url in urls:
        proxy = get_random_proxy()
        ua = get_random_user_agent() 
        driver = init_driver(proxy, user_agent=ua)
        try:
            driver.get(url)
            Bacotan_Random = random.choice(Tumpukan_Bacotan)
            
            Tempat_Bacot = find_element_by_multiple_attributes(driver, 'textarea', ['data-sf-role=comments-new-message', 'placeholder=Leave a comment'])
            if Tempat_Bacot:
                random_delay(2, 4)
                Tempat_Bacot.clear()
                random_delay()
                Tempat_Bacot.send_keys(Bacotan_Random["Bacot"])

            nama_field = find_element_by_multiple_attributes(driver, 'input', ['data-sf-role=comments-new-name', 'placeholder=Your name'])
            if nama_field:
                nama_field.clear()
                random_delay()
                nama_field.send_keys(Bacotan_Random["ManusiaBaik"])

            email_field = find_element_by_multiple_attributes(driver, 'input', ['data-sf-role=comments-new-email', 'placeholder=Email (optional)'])
            if email_field:
                email_field.clear()
                random_delay()
                email_field.send_keys(Bacotan_Random["AlamatPalsu"])

            try:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-sf-role="comments-new-submit-button"]'))
                )
                random_delay()
                submit_button.click()
                print(green_text.format(urls=url, proxy=proxy, ua=ua))
                log_result("done", url, proxy, ua)
            except TimeoutException:
                print(red_texts[0].format(urls=url, proxy=proxy, ua=ua))
                log_result("fail", url, proxy, ua)

            time.sleep(20)
        except WebDriverException:
            print(red_texts[1].format(urls=url, proxy=proxy, ua=ua))
        finally:
            driver.quit()

    print(red_texts[2])

def nofollow(urls, Koleksi_Bacotan):
    Tumpukan_Bacotan = Coba_GueLiat_Dulu(Koleksi_Bacotan)

    for url in urls:
        proxy = get_random_proxy()
        ua = get_random_user_agent() 
        driver = init_driver(proxy, user_agent=ua)
        try:
            driver.get(url)
            Bacotan_Random = random.choice(Tumpukan_Bacotan)

            komentar_section = find_element_by_multiple_attributes(driver, 'form', ['id=comment', 'class=comment-form', 'name=comment'])
            if not komentar_section:
                print(red_texts[3].format(urls=url, proxy=proxy, ua=ua))
                continue

            nama_field = find_element_by_multiple_attributes(driver, 'input', ['id=author', 'name=author', 'class=name'])
            if nama_field:
                nama_field.clear()
                random_delay()
                nama_field.send_keys(Bacotan_Random["ManusiaBaik"])

            email_field = find_element_by_multiple_attributes(driver, 'input', ['id=email', 'name=email', 'class=email'])
            if email_field:
                email_field.clear()
                random_delay()
                email_field.send_keys(Bacotan_Random["AlamatPalsu"])

            website_field = find_element_by_multiple_attributes(driver, 'input', ['id=url', 'name=url', 'class=website'])
            if website_field:
                website_field.clear()
                random_delay()
                website_field.send_keys(Bacotan_Random["TembakLink"])

            Tempat_Bacot = find_element_by_multiple_attributes(driver, 'textarea', ['id=comment', 'name=comment', 'class=comment'])
            if Tempat_Bacot:
                Tempat_Bacot.clear()
                random_delay()
                Tempat_Bacot.send_keys(Bacotan_Random["Bacot"])

            submit_button = find_element_by_multiple_attributes(driver, 'input', ['id=submit', 'name=submit', 'type=submit', 'class=submit'])
            if not submit_button:
                submit_button = find_element_by_multiple_attributes(driver, 'button', ['type=submit', 'class=submit', 'id=submit'])

            if submit_button:
                submit_button.click()
                print(green_text.format(urls=url, proxy=proxy, ua=ua))
                log_result("done", url, proxy, ua)
            else:
                print(red_texts[0].format(urls=url, proxy=proxy, ua=ua))
                log_result("fail", url, proxy, ua)

            time.sleep(20)
        except WebDriverException:
            print(red_texts[1].format(urls=url, proxy=proxy, ua=ua))

        finally:
            driver.quit()
    print(red_texts[4])

def main():
    print(banner)
    print(red_texts[5])
    print(red_texts[6])
    print(red_texts[7])
    pilihan = input(red_texts[8] + " ").strip()

    if pilihan == "1":
        proxies = update_proxies()
        print(f"[INFO] {len(proxies)} proxies updated & saved.")  
        user_agent_file = update_user_agents()
        print(f"[INFO] User-Agent file updated: {user_agent_file}")
        urls = [
            "https://appeals.cuyahogacounty.gov/about-us/judges/judge-sean-c-gallagher/eighth-district-court-of-appeals",
            "https://bebasata.qnb.com.eg/transfers/Gold-debit-becard",
            "https://conwayintranet.mhpteamsi.com/home/conway-regional/2021/03/01/ay-magazine%27s-best-of-2021?",
        ]
        dofollow(urls, "dofollow.json")
        
    elif pilihan == "2":
        proxies = update_proxies()
        print(f"[INFO] {len(proxies)} proxies updated & saved.")
        user_agent_file = update_user_agents()
        print(f"[INFO] User-Agent file updated: {user_agent_file}")        
        urls = [
            "https://www.ub.edu/multilingua/resultats-de-la-matricula-de-rosetta-stone/",
            "https://www.ocf.berkeley.edu/~paultkim/will-kobo-release-a-forma-2-in-2020/",
            "https://www.mae.gov.bi/en/visit-to-burundi-of-a-delegation-from-the-african-union-commission/",
        ]
        nofollow(urls, "nofollow.json")

    elif pilihan == "3":
        print(red_texts[9])

    elif pilihan.isalpha():
        print(red_texts[10])
    
    elif not pilihan.isalnum():
        print(red_texts[11])
        
    else:
        print(red_texts[12])

if __name__ == "__main__":
    main()