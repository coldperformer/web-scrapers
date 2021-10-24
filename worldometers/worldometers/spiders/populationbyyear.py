import scrapy
import logging
from ..items import PopulationByYearItem
from scrapy.utils.project import get_project_settings

class PopulationbyyearSpider(scrapy.Spider):
    name = 'populationbyyear'
    allowed_domains = ['www.worldometers.info']
    custom_settings = {'ITEM_PIPELINES': {'worldometers.pipelines.PopulationByYearPipeline': 300}}

    settings = get_project_settings()
    header_ua = settings.get('HEADERS_UA')
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.worldometers.info/world-population/world-population-by-year', 
        callback=self.parse, headers=self.header_ua)

    def parse(self, response):

        items = PopulationByYearItem()
        logging.info(msg=response.status)
        rows = response.xpath('//table/tbody/tr')
        
        for row in rows:
            items['year'] = row.xpath('.//td[1]/text()').get()
            items['world_population'] = row.xpath('.//td[2]/text()').get()
            items['yearly_change'] = row.xpath('.//td[3]/text()').get()
            items['net_change'] = row.xpath('.//td[4]/text()').get()
            items['density_per_kmsq'] = row.xpath('.//td[5]/text()').get()
            items['urban_pop'] = row.xpath('.//td[6]/text()').get()
            items['urban_pop_percent'] = row.xpath('.//td[7]/text()').get()

            yield items
