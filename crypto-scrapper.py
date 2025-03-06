import requests
from bs4 import BeautifulSoup
import feedparser

def scrape_coindesk():
    url = "https://www.coindesk.com/markets/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", class_="card-title")
    news = []
    for article in articles[:10]:
        title = article.get_text(strip=True)
        link = article["href"] if article["href"].startswith("http") else "https://www.coindesk.com" + article["href"]
        news.append((title, link))
    return news

def scrape_cointelegraph():
    url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(url)
    news = [(entry.title, entry.link) for entry in feed.entries[:10]]
    return news

def scrape_reuters():
    url = "https://www.reuters.com/markets/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", class_="story-title")
    news = []
    for article in articles[:10]:
        title = article.get_text(strip=True)
        link = article["href"] if article["href"].startswith("http") else "https://www.reuters.com" + article["href"]
        news.append((title, link))
    return news

def scrape_decrypt():
    url = "https://decrypt.co/feed"
    feed = feedparser.parse(url)
    news = [(entry.title, entry.link) for entry in feed.entries[:10]]
    return news

def scrape_fxstreet():
    url = "https://www.fxstreet.com/cryptocurrencies/news"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", class_="article-link")
    news = []
    for article in articles[:10]:
        title = article.get_text(strip=True)
        link = article["href"] if article["href"].startswith("http") else "https://www.fxstreet.com" + article["href"]
        news.append((title, link))
    return news

def main():
    sources = {
        "CoinDesk": scrape_coindesk,
        "CoinTelegraph": scrape_cointelegraph,
        "Reuters": scrape_reuters,
        "Decrypt": scrape_decrypt,
        "FXStreet": scrape_fxstreet,
    }
    
    for source, scraper in sources.items():
        print(f"\nNoticias de {source}:")
        news = scraper()
        if not news:
            print("No news were found.")
        for title, link in news:
            print(f"- {title}: {link}")

if __name__ == "__main__":
    main()
