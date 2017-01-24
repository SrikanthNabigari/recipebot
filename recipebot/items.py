# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EpicuriousRecipe(scrapy.Item):
    source_name = scrapy.Field()
    source_link = scrapy.Field()
    recipe_link = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    desc = scrapy.Field()
    ingredients = scrapy.Field()
    preparation = scrapy.Field()
    author = scrapy.Field()
    nutrition = scrapy.Field()
    
class YummlyRecipe(scrapy.Item):
    source_name = scrapy.Field()
    source_link = scrapy.Field()
    source_logo = scrapy.Field()
    recipe_link = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    desc = scrapy.Field()
    ingredients = scrapy.Field()
    preparation = scrapy.Field()
    author = scrapy.Field()
    nutrition = scrapy.Field()
    servings = scrapy.Field()

class BBCRecipe(scrapy.Item):
    source_name = scrapy.Field()
    source_link = scrapy.Field()
    source_logo = scrapy.Field()
    recipe_link = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    desc = scrapy.Field()
    ingredients = scrapy.Field()
    preparation = scrapy.Field()
    author = scrapy.Field()
    nutrition = scrapy.Field()