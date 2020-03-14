# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import time
 
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\\kcast\\predj\\predj')
import items


class PredjspiderSpider(scrapy.Spider):
    name = 'predjspider'
    allowed_domains = ['www.ijarcsee.org/index.php/IJARCSEE/article/view/']
  #  start_urls = ['http://www.ijarcsee.org/index.php/IJARCSEE/article/view/']
    ASIN = list(range(2,607))
    ASIN = [str(i) for i in ASIN]

    def start_requests(self):
        for i in self.ASIN:
            req = Request('http://www.ijarcsee.org/index.php/IJARCSEE/article/view/'+i,callback = self.parse_article)
            # Wait for 5 seconds
            time.sleep(.5)
            yield req

    def parse_article(self, response):
        item = items.PredjItem()
        item['title'] = response.xpath("//div[@id='articleTitle']/h3/text()").get()
        item['author'] = response.xpath("//div[@id='authorString']/em/text()").get()
        item['abstract'] = response.xpath("//div[@id='articleAbstract']/div/text()").getall()
        item['year'] = response.xpath("//div[@id='breadcrumb']/a/text()").getall()
        return item

    #print(response.xpath("//div[@id='articleTitle']/h3/text()").get())
    #print(response.xpath("//div[@id='authorString']/em/text()").get())
    #print(response.xpath("//div[@id='articleAbstract']/div/text()").get())
    #print(response.xpath("//div[@id='breadcrumb']/a/text()").get())