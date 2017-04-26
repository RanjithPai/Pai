from scrapy import Spider
from time import sleep
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
class ProductsSpider(Spider):
	name = "men"
        allowed_domains = ["mynthra.com"]
        start_urls = ['http://www.myntra.com/men-tshirts?src=tNav']
	def parse(self, response):
		driver = webdriver.Firefox(executable_path='/home/biodiv/geckodriver')
	    	driver.get('http://www.myntra.com/men-tshirts?src=tNav')	
		
	       
			
		sel=Selector(text=driver.page_source)
		products=sel.xpath('//*[@class="product-base"]/a')
		
		#print (products)
		for product in products:
			url=product.xpath('.//@href').extract()
			brand=product.xpath('.//*[@class="product-brand"]/text()').extract()
			description=product.xpath('.//*[@class="product-product"]/text()').extract()
			actual_price=(product.xpath('.//*[@class="product-strike"]/text()').extract() or product.xpath('.//*[@class="product-price"]/span/text()').extract()) 
			
				
			discount_price=(product.xpath('.//*[@class="product-discountedPrice"]/text()').extract() or product.xpath('.//*[@class="product-price"]/span/text()').extract())
			discount_percentage=product.xpath('.//*[@class="product-discountPercentage"]/text()').extract()

			yield{
			'Url':url,
			'brand':brand,
			'Description':description,
			'Actual_price':actual_price,
			'Discount_price':discount_price,
			'Discount_percentage':discount_percentage}
			
