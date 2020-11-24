import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'fruits'
    start_urls = ['https://www.halfyourplate.ca/fruits-and-veggies/fruits-a-z/']

    def parse(self, response):
        self.log(f'The response is {response.url}')
        fruits=response.css('.left-column ul li')
        for fruit in fruits:
            item = {
                'name':fruit.css('a::text').get(),

                
                'link':response.urljoin(fruit.css('div span a img::attr(src)').get()),
                
            }
            yield (item)
