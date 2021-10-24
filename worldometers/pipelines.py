# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter
from scrapy import signals
import logging


class WorldometersPipeline:

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.open_spider, signals.spider_opened)
        crawler.signals.connect(pipeline.close_spider, signals.spider_closed)
        return pipeline

    def open_spider(self, spider):
        logging.warning("--------------------SPIDER OPENED FROM PIPELINE--------------------")
        self.results_csv = open('populationbycountry.csv', 'w+b')
        self.results_exporter = CsvItemExporter(file=self.results_csv)
        self.results_exporter.start_exporting()
    
    def close_spider(self, spider):
        logging.warning("--------------------SPIDER CLOSED FROM PIPELINE--------------------")
        self.results_exporter.finish_exporting()
        self.results_csv.close()

    def process_item(self, item, spider):
        self.results_exporter.export_item(item)
        return item
