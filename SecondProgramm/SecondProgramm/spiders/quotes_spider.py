# Quotes second webpage
import scrapy 

class Quotes_Spider(scrapy.Spider) :
    name = "quotes" 
    
    allowed_domains = ['www.worldometers.info']
    start_urls =  ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self,response):

        rows = response.xpath('//tr')
        
        for row in rows :
            countries = row.xpath("./td/a/text()").get()
            population = row.xpath("./td[3]/text()").get()

            yield {
                'Countries' : countries,
                'Population' : population
            }
