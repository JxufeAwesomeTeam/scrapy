# -*- coding: utf-8 -*-
import scrapy
import re
import json


class YouGoodSpider(scrapy.Spider):
    name = 'you_good'
    allowed_domains = ['you.163.com']
    start_urls = ['http://you.163.com/']

    def parse(self, response):

        good_text = response.xpath("//script[contains(text(),'JSON_DATA_FROMFTL')]/text()").extract()[0].strip()[32:-1].split('//其他数据')[0].replace('\n','')  # 大类下的json数据

        attrList = re.match('.+attrList.+(\[.*\]).*autoOnsaleTime',good_text).group(1)
        #详情数据 [{'attrName':...,"attrValue":...},...]

        detailHtml = re.match('.+detailHtml.+?(\<.*\>).*picUrl1',good_text).group(1)
        #图片介绍" <p><img src=\"http://yanxuan.nosdn.127.net/***.jpg\" _src=\"http://yanxuan.nosdn.127.net/***.jpg\" style=\"\"/><\/p>..."

        pirUrls = re.match('.+("picUrl1.+),"seoDesc',good_text).group(1)
        #商品图片(后四张) "'picUrl1':"http://yanxuan.nosdn.127.net/***.jpg",..."

        skuList = re.match('.+skuList.*?(\[.*\]).*skuMap',good_text).group(1)
        #库存量(多种属性) [{...}...] 有很多属性
