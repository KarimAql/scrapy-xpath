import scrapy


class MedalistsSpider(scrapy.Spider):
    name = "medalists"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://wikipedia.org"]

    def parse(self, response):
        pass
