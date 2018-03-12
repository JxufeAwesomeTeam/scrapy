# coding = utf-8
import scrapy
from netease.items import NeteaseItem
import json

class neteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['you.163.com']
    start_urls = ['http://you.163.com/item/list?categoryId=1005000', #居家
                  'http://you.163.com/item/list?categoryId=1008000', #配件
                  'http://you.163.com/item/list?categoryId=1010000', #服装
                  'http://you.163.com/item/list?categoryId=1043000', #电器
                  'http://you.163.com/item/list?categoryId=1013001', #洗护
                  'http://you.163.com/item/list?categoryId=1005002', #饮食
                  'http://you.163.com/item/list?categoryId=1005001', #餐厨
                  'http://you.163.com/item/list?categoryId=1011000', #婴童
                  'http://you.163.com/item/list?categoryId=1019000', #文体
                  'http://you.163.com/item/list?categoryId=1065000', #特色区
                  ]

    def parse(self, response):
        goods_json = response.xpath("//script[contains(text(),'json_Data')]/text()").extract()[0].strip()[14:-1] #大类下的json数据
        dict_goods = json.loads(goods_json)  #json -> dict

        for goods in dict_goods['categoryItemList']:
            good_type = goods['category']['name']
            for good in goods['itemList']:

                item = NeteaseItem()

                item['type'] = good_type
                item['name'] = good['name']
                item['id'] = good['id']
                item['price'] = good['counterPrice']
                item['simpleDesc'] = good['simpleDesc']
                item['url'] = 'http://you.163.com/item/detail?id='+str(item['id'])

                yield item


