# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class NeteasePipeline(object):
    def process_item(self, item, spider):

        #with open('netease.txt','a') as fp:
        #   fp.write('商品名:'+item['name']+'\t\t,价格:'+str(item['price'])+'\t\t,类型:'+item['type']+'\t\t,简介:'+item['simpleDesc']+'\t\t,链接:'+item['url']+'\n')

        connection = pymysql.connect(host="localhost",
                             user="root",
                             password="123456",
                             db="netease_sql",
                             charset="utf8"
                             )
        try:
            cur = connection.cursor()

            sql = "INSERT INTO goods (name,id,type,url,price,simpleDesc) VALUES (%s,%s,%s,%s,%s,%s);"

            cur.execute(sql,(item['name'],item['id'],item['type'], item['url'], item['price'],item['simpleDesc']))

            connection.commit()
        finally:
            connection.close()
