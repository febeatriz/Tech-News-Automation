import logging
from scraper.base_extractor import BaseExtractor, Article
from scraper.extractors.hackernews import HackerNewsExtractor

logger = logging.getLogger(__name__)

class ScraperManager:
    def __init__(self, extractors: list[BaseExtractor] | None = None ):
        self.extractors = extractors or [
            HackerNewsExtractor(),
        ]

    def fetch_all(self, limit_per_source: int = 10) -> list[Article]:
        articles: list[Article] = []

        for extractor in self.extractors:
            try: 
                fetched = extractor.fetch_list(limit=limit_per_source)
                articles.extend(fetched)
                logger.info(
                    "Fetched %s articles from %s", 
                    len(fetched),
                    extractor.source_name,
                )
            except Exception:
                logger.exception(
                    "Error fetching articles from %s", extractor.source_name
                )

        return articles
