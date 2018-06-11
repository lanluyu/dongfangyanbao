# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DfyanbaoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    data_code = Field()
    data_name = Field()
    data_date = Field()
    data_report = Field()
    data_buy = Field()
    data_organization = Field()
    data_earnings18 = Field()
    data_earnings19 = Field()

