from scraper.manager import ScraperManager

manager = ScraperManager()
articles = manager.fetch_all(limit_per_source=5)

for article in articles:
    print(f"Title: {article.title}")
    print(f"URL: {article.url}")
    print(f"Source: {article.source}")
    print(f"Published At: {article.published_at}")
    print("-" * 40)
    print(f"[{article.source}] {article.title} - {article.url}")