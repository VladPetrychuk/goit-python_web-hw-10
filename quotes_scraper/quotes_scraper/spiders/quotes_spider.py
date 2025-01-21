import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = ["http://quotes.toscrape.com/"]

    authors = {}

    def parse(self, response):
        # Збір цитат із поточної сторінки
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author_name = quote.css("span small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            yield {
                "quote": text,
                "author": author_name,
                "tags": tags,
            }

            # Перевірка чи автор вже збережений
            if author_name not in self.authors:
                author_url = quote.css("span a::attr(href)").get()
                if author_url:
                    author_page = response.urljoin(author_url)
                    yield scrapy.Request(author_page, callback=self.parse_author)

        # Перехід на наступну сторінку
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        # Збір даних про автора
        name = response.css("h3.author-title::text").get().strip()
        birth_date = response.css("span.author-born-date::text").get()
        birth_location = response.css("span.author-born-location::text").get()
        description = response.css("div.author-description::text").get().strip()

        self.authors[name] = {
            "fullname": name,
            "born_date": birth_date,
            "born_location": birth_location,
            "description": description,
        }