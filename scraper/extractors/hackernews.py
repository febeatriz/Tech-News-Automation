# scraper/extractors/hackernews.py
import requests
from datetime import datetime
from scraper.base_extractor import BaseExtractor, Article
from config.settings import settings


class HackerNewsExtractor(BaseExtractor):
    source_name = "Hacker News"
    TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

    def fetch_list(self, limit: int = 10) -> list[Article]:
        ids = requests.get(self.TOP_STORIES_URL, timeout=settings.REQUEST_TIMEOUT).json()
        articles = []
        for story_id in ids[:limit]:
            item = requests.get(
                self.ITEM_URL.format(story_id), timeout=settings.REQUEST_TIMEOUT
            ).json()
            if not item or "url" not in item:
                continue
            articles.append(
                Article(
                    title=item.get("title", ""),
                    url=item["url"],
                    source=self.source_name,
                    published_at=datetime.fromtimestamp(item.get("time", 0)),
                )
            )
        return articles

    def fetch_content(self, article: Article) -> Article:
        # Hacker News só linka pra fora; conteúdo completo fica pra uma fase futura
        # (ex: usar readability/trafilatura). Por ora, deixamos vazio.
        article.content = None
        return article