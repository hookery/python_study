# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TesthkItem(scrapy.Item):
    #药物名称
    Product_Name=scrapy.Field()
    #注册号
    Registration_No=scrapy.Field()
    #持证商
    Certificate_Holder=scrapy.Field()
    #持证商地址
    Certificate_Holder_Address=scrapy.Field()
    #是否是毒药
    Legal_Classification=scrapy.Field()
    #是否属处方药
    Sale_Requirement=scrapy.Field()
    #成分
    Active_Ingredient =scrapy.Field()
    #注册日期
    Date_of_Registration=scrapy.Field()
    pass
