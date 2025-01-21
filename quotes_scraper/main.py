import os, json
from scrapy.crawler import CrawlerProcess
from quotes_scraper.spiders.quotes_spider import QuotesSpider

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "quotes.json": {"format": "json", "encoding": "utf-8", "overwrite": True},
        }
    })
    process.crawl(QuotesSpider)
    process.start()

    # Після завершення записуємо авторів у authors.json
    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(QuotesSpider.authors, f, ensure_ascii=False, indent=4)