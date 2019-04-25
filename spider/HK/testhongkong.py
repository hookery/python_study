# -*- coding: utf-8 -*-
import scrapy
from testHK.items import TesthkItem
from scrapy import FormRequest
from scrapy import Request

download=0
class TesthongkongSpider(scrapy.Spider):
    name = 'testhongkong'
    allowed_domains = ['drugoffice.gov']
    start_urls ='http://www.drugoffice.gov.hk/gb/unigb/www.drugoffice.gov.hk/eps/drug/productSearchOneFieldAction'
    initialdata = {
        "keyword": "A",
        "searchType": "O",
        "pageNoRequested": '1',
        "userType": "E",
        "fromLang": "tc",
        "fromSection": "consumer",
        "submit_drugsearch": "提交",
        "perPage": "20"
    }
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

    def start_requests(self):
        res = FormRequest(headers=self.head, url=self.start_urls, formdata=self.initialdata,callback=self.parse)
        print("start_requests")
        yield res


    def parse(self,response):
        pagenumberlist = response.xpath('//select[@id="pageNoRequested"]/option')
        pagenumber = len(pagenumberlist)
        for i in range(1,pagenumber+1):
            data = {
                "keyword": "A",
                "searchType": "O",
                "pageNoRequested": str(i),
                "userType": "E",
                "fromLang": "tc",
                "fromSection": "consumer",
                "submit_drugsearch": "提交",
                "perPage": "20"
            }
            yield FormRequest(headers=self.head,url=self.start_urls,formdata=data,callback=self.getlink,dont_filter=True)



    def getlink(self,response):
        linklist = response.xpath('//tr[@valign="middle"]/td[2]/a/@href').extract()
        for url in linklist:
            global download
            download=download+1
            print("目前已经爬取了%s条数据了"%str(download))
            detail = Request(url=url, headers=self.head,callback=self.parse_detail,dont_filter=True)
            yield detail



    def parse_detail(self,response):
        Active_Ingredient=[]
        info=response.xpath("//table[@style='width:600px;']/tr[position()<11 and position()>2]/td[3]")
        Product_Name=info[0].xpath("./text()").extract()[1].strip()
        Registration_No=info[1].xpath("./text()").extract()[0].strip()
        Certificate_Holder=info[2].xpath("./text()").extract()[0].strip()
        Certificate_Holder_Address=info[3].xpath("./text()").extract()[0].strip()
        Legal_Classification=info[4].xpath("./text()").extract()[0].strip()
        Sale_Requirement=info[5].xpath("./text()").extract()[0].strip()
        last_ingredient=info.xpath(".//table[@id='ingredientTable']//td/text()").extract()
        for each_ingredient in last_ingredient:
            Active_Ingredient.append(each_ingredient.strip())
        Date_of_Registration=info[7].xpath("./text()").extract()[0].strip()
        item=TesthkItem(Product_Name=Product_Name,Registration_No=Registration_No,Certificate_Holder=Certificate_Holder,Certificate_Holder_Address=Certificate_Holder_Address,Legal_Classification=Legal_Classification,Sale_Requirement=Sale_Requirement,Active_Ingredient=Active_Ingredient,Date_of_Registration=Date_of_Registration)
        yield item
