import scrapy
from recipebot.items import BBCRecipe
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request, Response
import itertools

class RecipeLink(scrapy.Spider):
    name = "bbcgfrecipebot"
    allowed_domains = ["bbcgoodfood.com"]
    start_urls = ["http://www.bbcgoodfood.com/recipes/category/healthy"]

    def parse(self, response):
        sites = response.xpath('//a[contains(@href, "/recipes/collection")]')
        for sel in sites:
            item = sel.xpath('@href').extract()
            for link in item:
                link = link
            url = "http://www.bbcgoodfood.com%s" % link
            yield Request(url, callback = self.parse2)

    def parse2(self, response):
        sites = response.xpath('//a[contains(@href, "/recipes/")]')
        for sel in sites:
            item = sel.xpath('@href').extract()
            for link in item:
                link = link
            url = "http://www.bbcgoodfood.com%s" % link
            yield Request(url, callback = self.parseCategory)

    def parseCategory(self,response):
        sel = response
        item = BBCRecipe()
        item['source_name'] = "bbcgoodfood"
        item['source_link'] = "http://www.bbcgoodfood.com"
        item['recipe_link'] = response.url
        item['source_logo'] = sel.xpath('//div[@id="main-gf-logo"]/a/img/@src').extract_first()
        item['name'] = sel.xpath('//h1[@class="recipe-header__title"]/text()').extract_first()
        item['image'] = sel.xpath('//div[@class="img-container ratio-11-10"]/img/@src').extract_first()
        item['desc'] = sel.xpath('//div[@class="field-item even"]/text()').extract_first()
        item['ingredients'] = sel.xpath('//li[@class="ingredients-list__item"]/text()/following-sibling::a/text()').extract()
        item['preparation'] = sel.xpath('//li[@class="method__item"]/p/text()').extract()
        item['author'] = sel.xpath('//span[@class="author"]/a/text()').extract_first()
        nutri_label = sel.xpath('//span[@class="nutrition__label"]/text()').extract()
        nutri_value = sel.xpath('//span[@class ="nutrition__value"]/text()').extract()
        n_l = (s.strip() for s in nutri_label)
        n_v = (s.strip() for s in nutri_value)
        item['nutrition'] = dict(zip(n_l,n_v))
        yield item

