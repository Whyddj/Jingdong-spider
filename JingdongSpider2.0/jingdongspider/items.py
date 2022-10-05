# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    a_id = scrapy.Field()
    b_time = scrapy.Field()
    c_comment = scrapy.Field()
