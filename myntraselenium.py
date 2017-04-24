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
		product=sel.xpath('//*[@class="product-base"]')
		print product
