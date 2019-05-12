import scrapy


class QuotesSpider(scrapy.Spider):
    name = "main-page"

    def start_requests(self):
        urls = [
            'https://news.ycombinator.com/news?p=1',
            'https://news.ycombinator.com/news?p=2',
            'https://news.ycombinator.com/news?p=3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css('table.itemlist').getall()
        print(table)