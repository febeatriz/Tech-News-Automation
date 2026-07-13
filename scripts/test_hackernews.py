from scraper.extractors.hackernews import HackerNewsExtractor

extractor = HackerNewsExtractor()
articles = extractor.fetch_list(limit=5)
for a in articles:
    print(a.title, "-", a.url)