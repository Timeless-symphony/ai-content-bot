import requests
import json
from config import NEWS_API_KEY

def fetch_ai_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence",
        "language": "en",
        "pageSize": 5,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url, params=params)
    articles = response.json()["articles"]

    # Convert to a simplified list of dicts
    simplified_articles = [
        {"title": a["title"], "url": a["url"], "content": a["content"]}
        for a in articles if a["content"]
    ]

    # Save to JSON file
    with open("fetched_news.json", "w", encoding="utf-8") as f:
        json.dump(simplified_articles, f, indent=2, ensure_ascii=False)

    #print(" Fetched news saved to fetched_news.json")

    return [{"title": a["title"], "url": a["url"], "content": a["content"]} for a in articles]



if __name__ == "__main__":
    print(fetch_ai_news())

