from scrapy import Spider
from time import sleep
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
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
		while True:
			try:
				next_page=self.driver.find_element_by_xpath('//div[@class="results-showmore"]')
				sleep(3)
				self.logger.info('Sleeping for 3 seconds')
				next_page.click() 
				sel=Selector(text=self.driver.page_source)
				products=sel.xpath('//*[@class="product-base"]/a/@href').extract()

		
				for product in products:
					url='http://www.myntra.com/'+product
					yield Request(url,callback=self.parse_book)
			except NoSuchElementException:
				self.logger.info('No more elements to display')
				self.driver.quit()
				break
		
	def parse_book(self,response):
		pass
