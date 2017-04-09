import scrapy

class TripsSpider(scrapy.Spider):
    name = 'trips'
    start_urls = ['https://www.tripadvisor.com/317493']
    download_delay = 1.5
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'title': response.css('div.header_container h1#HEADING ::text')[1].extract(),
            'rating': response.css('div.header_container div.rating ::text').extract(),
            'order': response.css('div.header_container div.slim_ranking ::text').extract()
        }

    def clean(self, input_list): 
        while "\n" in input_list: input_list.remove("\n")
        return input_list