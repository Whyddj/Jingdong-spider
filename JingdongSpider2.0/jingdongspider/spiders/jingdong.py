import scrapy
from scrapy import Request
from ..items import JingdongItem
import json


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['jd.com']

    def start_requests(self):
        for page in range(100):
            yield Request(url=f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1')

    def parse(self, response):
        data = response.text.lstrip('fetchJSON_comment98(').rstrip(');')
        jsondata = json.loads(data)
        jingdong_item = JingdongItem()
        for x in jsondata['comments']:
            jingdong_item['a_id'] = x['id']
            jingdong_item['c_comment'] = x['content'].replace('\n', ' ')
            jingdong_item['b_time'] = x['creationTime']
            yield jingdong_item