from scrapy import Spider

from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import Request

class NikeSpider(Spider):
	name = "men"
        allowed_domains = ["myntra.com"]
        start_urls = ['www.myntra.com/men-tshirts?src=tNav']
        
        def start_requests(self):
        	self.driver = webdriver.Firefox(executable_path='/home/biodiv/geckodriver')
    		self.driver.get('http://www.myntra.com/men-tshirts?src=tNav')
		sel=Selector(text=self.driver.page_source)
		products=sel.xpath('//*[@class="product-base"]/a/@href').extract()

		
		for product in products:
			url='http://www.myntra.com/'+product
			yield Request(url,callback=self.parse_book) 
	def parse_book(self,response):
		pass
