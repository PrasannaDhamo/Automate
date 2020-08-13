import requests

NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_news(news_api_key: str) -> None:
    # fetching a list of articles in json format
    news_page = requests.get(NEWS_API + news_api_key).json()
    # each article in the list is a dict
    for i, article in enumerate(news_page["articles"], 1):
        print(f"{i}.) {article['title']}")


if __name__ == "__main__":
    fetch_news(news_api_key="41cf764c2b004e86a134fa459b1b7db8")
