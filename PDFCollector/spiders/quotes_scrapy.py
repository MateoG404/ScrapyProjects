''' Script to collect the PDF links for the thesis '''

import scrapy

class quotes_scrapy(scrapy.Spider): 

    # Atributes

    name = "thesis_postgraduate"

    allowed_domains = ['https://repositorio.unal.edu.co/handle/unal/']
    start_urls = ['https://repositorio.unal.edu.co/handle/unal/77950']

    def parse(self,response):

        number_thesis = 77950
        
        
        ''' Get the information about the Thesis '''

        name_pdf = response.xpath('//html/body/div[4]/div/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/a/text()').get()
        title = response.xpath('/html/body/div[4]/div/div/div[1]/div/div[1]/div/h2/text()').get()

        ''' Save exactly the name of the PDF without the memory space.
            
            Example : 
            We get the next name of PDF : 1015439326.2020.pdf (2.481Mb) . And we have to delete (2.481Mb)
            with the next part of code.
            
        '''
        
        substring = 'pdf'
        position_substring = name_pdf.index(substring)
        name_pdf = name_pdf[:position_substring+3].strip()
        
        
        link_pdf = 'https://repositorio.unal.edu.co/bitstream/handle/unal/' + str(number_thesis) + '/' + name_pdf + '?sequence=4&isAllowed=y'


        yield {
            'Title Thesis' : title,
            'Name PDF' : name_pdf,
            'Link PDF' : link_pdf
        }
    
    