# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtaTurnstileSpiderItem(scrapy.Item):

    week_url = scrapy.Field()
    turnstile_recordings = scrapy.Field()
    # c_a = scrapy.Field()
    # unit = scrapy.Field()
    # scp = scrapy.Field()
    # station = scrapy.Field()
    # linename = scrapy.Field()
    # division = scrapy.Field()
    # date = scrapy.Field()
    # time = scrapy.Field()
    # desc = scrapy.Field()
    # entries = scrapy.Field()
    # exits = scrapy.Field()
