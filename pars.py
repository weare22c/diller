
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent

def google_search(domain):
    file = open("targs.txt", "w")
    ua = UserAgent()
    for i in range(10):  # Здесь можно установить лимит страниц
        url = f"https://www.google.com/search?q=site:*.{domain}/wp-login.php&start={i * 10}"
        headers = {"User-Agent": ua.random}
        soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for link in soup.find_all("a"):
            url = link.get("href")
            if "url?q=" in url and "/search?q=" not in url:
                file.write(url.split("url?q=")[1].split("&sa=U&")[0] + "\n")
        time.sleep(1)  # Пауза между запросами, чтобы избежать блокировки
    file.close()

if __name__ == "__main__":
    domain = input("Введите домен (se, ru, cz, etc.): ")
    google_search(domain)
