# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy import FormRequest
from tx3.items import Tx3Item
import json

class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['tx3.cbg.163.com']
    start_urls = ['http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search']
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }

    def start_requests(self):
        url = "https://tx3.cbg.163.com/cgi-bin/search.py"
        data = {
            "act": "overall_search_role",
            "order_by": "",
            "page": "1",
            "other_arg": "",
            "school": "5",
            "price_max": "500000",
            "equip_level_min": "80",
            "equip_level_max": "80",
            "critical": "2000",
            "mattack_max": "3000",
            "castspeed": "38"
        }
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Refer": "https://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search"
        }

        res = FormRequest(url=url, headers=head, formdata=data, callback=self.parse)
        yield res

    def parse(self, response):
        # inspect_response(response, self)
        dicttype = json.loads(response.text)
        for each_account in dicttype["msg"]:
            item = Tx3Item()
            item["each_info"] = each_account
            serve_id = each_account["serverid"]
            equip_id = each_account["equipid"]
            item["url"] = r"https://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid="+str(serve_id)+r"&equip_id="+str(equip_id)
            yield item
