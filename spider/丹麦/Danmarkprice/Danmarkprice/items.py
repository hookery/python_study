# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DanmarkpriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # "Medicinal product"=scrapy.Field()
    Medicinal_product = scrapy.Field()
    Product_number = scrapy.Field()
    Strength = scrapy.Field()
    Package = scrapy.Field()
    Active_substance = scrapy.Field()
    Company = scrapy.Field()
    ATC_code = scrapy.Field()
    Dose_dispensing = scrapy.Field()
    Dispensing_groupe = scrapy.Field()
    Price_per_package = scrapy.Field()
    Price_per_unit = scrapy.Field()
    Price_per_defined_daily_dose = scrapy.Field()
    Pharmacy_cost_price = scrapy.Field()
    Reimbursement_calculated_from = scrapy.Field()

    pass
