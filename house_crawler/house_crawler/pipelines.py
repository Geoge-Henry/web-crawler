# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pandas as pd
from . import CRAWLER_DIR


class HouseCrawlerPipeline(object):

    def __init__(self):
        self.csv_file_path = CRAWLER_DIR + "/spiders/"
        self.csv_file = "house_crawler_data.csv"

    def process_item(self, item, spider):
        if item:
            csv_file = self.csv_file_path + self.csv_file
            file_obj = pd.DataFrame([item])
            if os.path.exists(csv_file):
                file_obj.to_csv(csv_file, mode='a', header=False,
                                encoding='utf-8-sig', index=False)
            else:
                file_obj.to_csv(csv_file, header=False,
                                encoding='utf-8-sig', index=False)
        return item
