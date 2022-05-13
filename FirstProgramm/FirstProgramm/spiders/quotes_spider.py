import scrapy

class QuotesScrapper(scrapy.Spider) :
    name = "quotes" # Name of the Spider

    def start_requests(self): # This class returns Responses about the pages that there are in URLS list
        
        allowed_domains = [] # Allowed Links
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ] # List with the name of some Webpages that will be scrapped

        for url in urls: # Return a Function Generator with the response of the websites
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): # Method to create text about the response created in start_request function

        page = response.url.split("/")[-2] # Return the name of the page

        # response.xpath('//tag[@atributo="Valor"]') # Example of search with xpath 
        # .getall() -> Get all the information
        
        
        print("page  --> " ,page) 
        
        filename = f'quotes-{page}.html' # Get the name of the filename 
        
        #Store the values of the page and filename
        
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')


    # Crawl Spider -> Hace indexo de paginas web
