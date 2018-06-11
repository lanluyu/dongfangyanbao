# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from dfyanbao.items import DfyanbaoItem


class DongfangSpider(Spider):
    name = 'dongfang'
    allowed_domains = ['http://data.eastmoney.com/report/']
    start_url = 'http://data.eastmoney.com/report/'

    def start_requests(self):
        for page in range(1,340):
            yield Request(url = self.start_url,callback=self.parse,meta={'page':page},dont_filter=True)

    def parse(self, response):
        a = response.xpath('.//span[@class="at"]/text()')
        print('正在爬取',a,'页')
        reports = response.xpath('.//*[@id="dt_1"]/tbody/tr')
        for report in reports:
            item = DfyanbaoItem()
            item['data_code'] = ''.join(report.xpath('.//td[3]/a/text()').extract()).strip()
            item['data_name'] = ''.join(report.xpath('.//td[4]/a/text()').extract()).strip()
            item['data_date'] = ''.join(report.xpath('.//td[2]/span/text()').extract()).strip()
            item['data_report'] = ''.join(report.xpath('.//td[6]/div/a/text()').extract()).strip()
            item['data_buy'] = ''.join(report.xpath('.//td[7]/text()').extract()).strip()
            item['data_organization'] = ''.join(report.xpath('.//td[9]/a/text()').extract()).strip()
            item['data_earnings18'] = ''.join(report.xpath('.//td[10]/text()').extract()).strip()
            item['data_earnings19'] = ''.join(report.xpath('.//td[12]/text()').extract()).strip()

            yield item
            print(item)

