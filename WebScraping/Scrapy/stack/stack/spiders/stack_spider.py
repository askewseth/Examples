from scrapy import Spider
from scrapy.selector import Selector
# Import from scrapy packages items.py file
from stack.items import StackItem


class StackSpider(Spider):
    """Spider for crawling stackoverflow."""
    # Define the name of the spider
    name = "stack"
    # Container for the base URLs for the allowed domains for the spider
    allowed_domains = ["stackoverflow.com"]
    # Start point for crawling
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        """Break apart the HTML using xpath."""
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            # item defined in items.py
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
