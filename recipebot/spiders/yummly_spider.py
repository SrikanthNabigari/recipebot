import scrapy
from recipebot.items import YummlyRecipe
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request, Response
import itertools

class RecipeLink(scrapy.Spider):
    name = "yummlyrecipebot"
    allowed_domains = ["yummly.com"]
    start_urls = ["http://www.yummly.co"]    

    def parse(self, response):
        sites = response.xpath('//a[contains(@href, "#href")]')
        for sel in sites:
            item = sel.xpath('@href').extract()
            for link in item:
                link = link
            url = "http://www.yummly.co%s" % link
            print url
            yield Request(url, callback = self.parseCategory)

    
    def parseCategory(self,response):
        sel = response
        item = YummlyRecipe()
        item['source_name'] = "Epicurious"
        item['source_link'] = "http://www.yummly.com"
        item['source_logo'] = sel.xpath('//a[@class="logo"]/img/@src').extract_first()
        item['recipe_link'] = response
        item['name'] = sel.xpath('//div[@class="primary-info-text"]/h1/text()').extract_first()
        item['image'] = sel.xpath('//div[@class="image-wrapper"]/img/@src').extract_first()

        ing_amount = sel.xpath('//div[@class="IngredientLine"]/span[@class="amount"]/span/span/text()').extract()
        ing_unit = sel.xpath('//div[@class="IngredientLine"]/span[@class="unit"]/text()').extract()
        ingredient = sel.xpath('//div[@class="IngredientLine"]/span[@class="ingredient"]/text()').extract()
        ing_remainder = sel.xpath('//div[@class="IngredientLine"]/span[@class="remainder"]/text()').extract()

        item['ingredients'] = sel.xpath().extract()
        item['servings'] = sel.xpath('//div[@class="servings"]/label/input/@value').extract()
        item['author'] = sel.xpath('//span[@class="attribution"]/a/text()').extract_first()
        
        print item
        yield item

