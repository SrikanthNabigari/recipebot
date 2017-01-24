import scrapy
from recipebot.items import EpicuriousRecipe
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request, Response
import itertools

class RecipeLink(scrapy.Spider):
    name = "epicuriousrecipebot"
    allowed_domains = ["epicurious.com"]
    start_urls = ["http://www.epicurious.com/search/?page=%s" % \
                  x for x in xrange(1,10)]    
                # you can maximize the range upto 2142
    def parse(self, response):
        sites = response.xpath('//a[@class="photo-link"][contains(@href, "/recipes/food/views")]')
        for sel in sites:
            item = sel.xpath('@href').extract()
            for link in item:
                link = link
            url = "http://www.epicurious.com%s" % link
            yield Request(url, callback = self.parseCategory)

 
    def parseCategory(self,response):
        sel = response
        item = EpicuriousRecipe()
        item['source_name'] = "Epicurious"
        item['source_link'] = "http://www.epicurious.com"
        item['recipe_link'] = response.url
        item['name'] = sel.xpath('//div[@class="title-source"]/h1/text()').extract_first()
        item['image'] = sel.xpath('//img[@class="photo loaded"]/@srcset').extract_first()
        item['desc'] = sel.xpath('//div[@class="dek"]/p/text()').extract_first()
        item['ingredients'] = sel.xpath('//li[@class="ingredient"]/text()').extract()
        item['preparation'] = sel.xpath('//li[@class="preparation-step"]/text()').extract()
        item['author'] = sel.xpath('//a[@class="contributor"]/text()').extract_first()
        nutri_label = sel.xpath('//span[@class="nutri-label"]/text()').extract()
        nutri_data = sel.xpath('//span[@class ="nutri-data"]/text()').extract()

        n_l = (s.strip() for s in nutri_label)
        n_d = (s.strip() for s in nutri_data)
        item['nutrition'] = dict(zip(n_l,n_d))
        yield item

