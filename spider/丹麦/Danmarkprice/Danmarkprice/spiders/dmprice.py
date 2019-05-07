# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from scrapy import Request
from scrapy.shell import inspect_response
from Danmarkprice.items import DanmarkpriceItem

download=0

class DmpriceSpider(scrapy.Spider):
    name = 'dmprice'
    allowed_domains = ['medicinpriser.dk']
    start_urls = ['https://medicinpriser.dk/default.aspx?lng=2']
    head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "medicinpriser.dk",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }

    def parse(self, response):
        post_url = 'https://medicinpriser.dk/default.aspx?lng=2'
        get_url='https://medicinpriser.dk/Default.aspx?Navn=%'
        VIEWSTATE = response.xpath("//input[@id='__VIEWSTATE']/@value").extract()
        EVENTTARGET = response.xpath("//input[@id='__EVENTTARGET']/@value").extract()
        EVENTARGUMENT = response.xpath("//input[@id='__EVENTARGUMENT']/@value").extract()
        VIEWSTATEGENERATOR = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").extract()
        EVENTVALIDATION = response.xpath("//input[@id='__EVENTVALIDATION']/@value").extract()
        LASTFOCUS=response.xpath("//input[@id='__LASTFOCUS']/@value").extract()
        CookieIDHiddenField = response.xpath("//input[@id='ctl00_Medicinliste_CookieIDHiddenField']/@value").extract()
        data = {
            '__EVENTTARGET': EVENTTARGET,
            '__EVENTARGUMENT': EVENTARGUMENT,
            '__LASTFOCUS': LASTFOCUS,
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': EVENTVALIDATION,
            'ctl00$ctl07$simpleForm$LaegemiddelBox': '%',
            'ctl00$ctl07$simpleForm$VirksomtstofBox': '',
            'ctl00$ctl07$simpleForm$StyrkeBox': '',
            'ctl00$ctl07$simpleForm$VarenummerBox': '',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$0': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$1': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$2': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$3': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$4': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$5': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$6': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$7': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$8': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$9': 'on',
            'ctl00$ctl07$simpleForm$SearchButton': 'Search',
            # 'ctl00$ctl07$Results$ColumnSelector$UpdateButton': 'Update',
            # 'ctl00$ctl07$Results$PagerTop$ResultsCountList': '10',
            # 'ctl00$ctl07$Results$PagerBottom$ResultsCountList': '10',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$0': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$1': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$5': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$6': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$7': 'on',
            'ctl00$Medicinliste$CookieIDHiddenField': CookieIDHiddenField
        }
        Cookie=response.headers.getlist('Set-Cookie')
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "medicinpriser.dk",
            "Upgrade-Insecure-Requests": "1",
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        # res = FormRequest(url=post_url, headers=head, formdata=data, callback=self.parse_realpage,dont_filter=True)
        res = Request(url=get_url, headers=head, callback=self.parse_realpage, dont_filter=True)
        yield (res)

    def parse_realpage(self, response):
        post_url='https://medicinpriser.dk/Default.aspx?Navn=%25'
        VIEWSTATE = response.xpath("//input[@id='__VIEWSTATE']/@value").extract()
        EVENTTARGET = response.xpath("//input[@id='__EVENTTARGET']/@value").extract()
        EVENTARGUMENT = response.xpath("//input[@id='__EVENTARGUMENT']/@value").extract()
        VIEWSTATEGENERATOR = response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").extract()
        EVENTVALIDATION = response.xpath("//input[@id='__EVENTVALIDATION']/@value").extract()
        LASTFOCUS = response.xpath("//input[@id='__LASTFOCUS']/@value").extract()
        CookieIDHiddenField = response.xpath("//input[@id='ctl00_Medicinliste_CookieIDHiddenField']/@value").extract()
        data = {
            '__EVENTTARGET': EVENTTARGET,
            '__EVENTARGUMENT': EVENTARGUMENT,
            '__LASTFOCUS': LASTFOCUS,
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': EVENTVALIDATION,
            'ctl00$ctl07$simpleForm$LaegemiddelBox': '%',
            'ctl00$ctl07$simpleForm$VirksomtstofBox': '',
            'ctl00$ctl07$simpleForm$StyrkeBox': '',
            'ctl00$ctl07$simpleForm$VarenummerBox': '',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$0': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$1': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$2': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$3': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$4': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$5': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$6': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$7': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$8': 'on',
            # 'ctl00$ctl07$Results$ColumnSelector$ColumnList$9': 'on',
            'ctl00$ctl07$Results$PagerTop$LinkRight': 'Next',
            # 'ctl00$ctl07$Results$ColumnSelector$UpdateButton': 'Update',
            # 'ctl00$ctl07$Results$PagerTop$ResultsCountList': '10',
            # 'ctl00$ctl07$Results$PagerBottom$ResultsCountList': '10',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$0': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$1': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$5': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$6': 'on',
            # 'ctl00$ctl07$ResultsCannabis$ColumnSelector$ColumnList$7': 'on',
            'ctl00$Medicinliste$CookieIDHiddenField': CookieIDHiddenField
        }
        Cookie = response.headers.getlist('Set-Cookie')
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "medicinpriser.dk",
            "Upgrade-Insecure-Requests": "1",
            "Cookie": Cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        lefttable = response.xpath("//div[@id='ctl00_ctl07_Results_LeftGridDiv']//tr")
        for each_drug in lefttable[1:]:
            product_number = each_drug.xpath("./td[1]/div/text()")[1].extract()
            url='https://medicinpriser.dk/Default.aspx?id=15&vnr='+product_number
            res = Request(url=url, headers=head, callback=self.parse_detail, dont_filter=True)
            yield res
        next_page = response.xpath("//input[@value='Next']")
        if next_page:
            yield FormRequest(url=post_url, formdata=data, headers=head, callback=self.parse_realpage, dont_filter=True)

    def parse_detail(self, response):
        # inspect_response(response, self)
        # names = locals()
        global download
        download=download+1
        print("正在爬取第%s条数据"%str(download))
        leftcontentkey = response.xpath("//div[@class='Produktfakta_Left']//tr[position()>1]/td[1]/span")
        leftcontentvalue = response.xpath("//div[@class='Produktfakta_Left']//tr[position()>1]/td[2]/span")
        rightcontentkey = response.xpath("//div[@class='Produktfakta_Right']//tr[@class='Produktfakta_Row']/td[1]//span")
        rightcontentvalue = response.xpath("//div[@class='Produktfakta_Right']//tr[@class='Produktfakta_Row']/td[2]//span")
        item = DanmarkpriceItem()
        item["Medicinal_product"] = "-"
        item["Product_number"] = "-"
        item["Strength"] = "-"
        item["Package"] = "-"
        item["Active_substance"] = "-"
        item["Company"] = "-"
        item["ATC_code"] = "-"
        item["Dose_dispensing"] = "-"
        item["Dispensing_groupe"] = "-"
        item["Price_per_package"] = "-"
        item["Price_per_unit"] = "-"
        item["Price_per_defined_daily_dose"] = "-"
        item["Pharmacy_cost_price"] = "-"
        item["Reimbursement_calculated_from"] = "-"
        for i in range(len(leftcontentkey)):
            if leftcontentkey[i].xpath("./text()").extract_first() == 'Medicinal product':
                item["Medicinal_product"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Product number':
                item["Product_number"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Strength':
                item["Strength"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Package ':
                item["Package"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Active substance':
                item["Active_substance"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Company':
                item["Company"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'ATC code':
                item["ATC_code"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Dose dispensing':
                item["Dose_dispensing"] = leftcontentvalue[i].xpath("./text()").extract_first()
            elif leftcontentkey[i].xpath("./text()").extract_first() == 'Dispensing groupe':
                item["Dispensing_groupe"] = leftcontentvalue[i].xpath("./text()").extract_first()
        for j in range(len(rightcontentkey)):
            if rightcontentkey[j].xpath("./text()").extract_first() == 'Price per package ':
                item["Price_per_package"] = rightcontentvalue[j].xpath("./text()").extract_first()
            elif rightcontentkey[j].xpath("./text()").extract_first() == 'Price per unit':
                item["Price_per_unit"] = rightcontentvalue[j].xpath("./text()").extract_first()
            elif rightcontentkey[j].xpath("./text()").extract_first() == 'Price per defined daily dose':
                item["Price_per_defined_daily_dose"] = rightcontentvalue[j].xpath("./text()").extract_first()
            elif rightcontentkey[j].xpath("./text()").extract_first() == 'Pharmacy cost price':
                item["Pharmacy_cost_price"] = rightcontentvalue[j].xpath("./text()").extract_first()
            elif rightcontentkey[j].xpath("./text()").extract_first() == 'Reimbursement calculated from':
                item["Reimbursement_calculated_from"] = rightcontentvalue[j].xpath("./text()").extract_first()
            # inspect_response(response, self)
        yield item