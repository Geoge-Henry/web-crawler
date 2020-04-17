# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/3/24 15:33
import scrapy
import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT_DIR))
sys.path.insert(0, os.path.join(ROOT_DIR, "house_crawler"))
sys.path.insert(0, os.path.join(ROOT_DIR, "house_crawler/house_crawler"))
from items import HouseCrawlerItem
import settings as my_settings


class HouseCrawlerSpider(scrapy.Spider):
    name = "house_crawler"
    allowed_domains = ["sz.ke.com"]
    start_urls = [
        "https://sz.ke.com/ershoufang/",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="sellListContent"]'):
            for item_infos in sel.xpath('//li[@class="clear"]/div[@class="info clear"]'):
                item = HouseCrawlerItem()
                house_info = item_infos.xpath('div[@class="address"]')
                item['house_name'] = house_info.xpath('div[@class="flood"]/div[@class="positionInfo"]/a/text()').extract()[0]
                item['total_price'] = house_info.xpath('div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()').extract()[0] + "万"
                item['link'] = item_infos.xpath('div[@class="title"]/a[@class="VIEWDATA CLICKDATA maidian-detail"]/@href').extract()[0]
                item['price'] = house_info.xpath('div[@class="priceInfo"]/div[@class="unitPrice"]/@data-price').extract()[0]
                yield item


crawler_settings = Settings()
crawler_settings.setmodule(my_settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(HouseCrawlerSpider)
# process.start(stop_after_crawl=False)
process.start()

