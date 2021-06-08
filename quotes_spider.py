import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com/page/1/',
                'https://quotes.toscrape.com/page/2/']

    def parse(self, response):
        qt = response.css('div.quote')
        for quote in qt:
            yield{'text': quote.css('span.text::text').get()}


