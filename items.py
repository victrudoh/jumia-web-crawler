# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommerceScraperItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    new_price = scrapy.Field() 
    old_price = scrapy.Field()
    disc_perc = scrapy.Field()
    rating = scrapy.Field()
    key_features = scrapy.Field()
    specs = scrapy.Field()
    imgs = scrapy.Field()
