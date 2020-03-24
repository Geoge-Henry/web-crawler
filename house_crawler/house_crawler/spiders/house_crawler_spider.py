# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/3/24 15:33
import scrapy
import sys
sys.path.append("..")
from items import HouseCrawlerItem


class HouseCrawlerSpider(scrapy.Spider):
    name = "house_crawler"
    allowed_domains = ["sz.fang.ke.com"]
    start_urls = [
        "https://sz.fang.ke.com/loupan",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            for item_infos in sel.xpath('//li[@class="resblock-list post_ulog_exposure_scroll has-results"]'):
                item = HouseCrawlerItem()
                item['title'] = item_infos.xpath('a[@class="resblock-img-wrapper "]/@title').extract()
                item['link'] = item_infos.xpath('a[@class="resblock-img-wrapper "]/@href').extract()
                item['price'] = item_infos.xpath('div[@class="resblock-desc-wrapper"]/div[@class="resblock-price"]/div[@class="main-price"]/span[@class="number"]/text()').extract()
                yield item
