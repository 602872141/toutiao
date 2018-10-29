# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaoItem(scrapy.Item):
    # define the fields for your item here like:
    id =  scrapy.Field()
    images = scrapy.Field()
    img_url=scrapy.Field()
    image_path=scrapy.Field()
    name=scrapy.Field()
    pass
