import scrapy
import logging
from ..items import PopulationByCountryItem
from scrapy.utils.project import get_project_settings

class PopulationbycountrySpider(scrapy.Spider):
    name = 'populationbycountry'
    allowed_domains = ['www.worldometers.info']
    custom_settings = {'ITEM_PIPELINES': {'worldometers.pipelines.PopulationByCountryPipeline': 300}}
    
    settings = get_project_settings()
    header_ua = settings.get('HEADERS_UA')
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.worldometers.info/world-population/population-by-country/', 
        callback=self.parse, headers=self.header_ua)

    def parse(self, response):

        countries = response.xpath('//td/a')

        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):


        items = PopulationByCountryItem()
        logging.info(msg=response.status)
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')

        for row in rows:
            items['country'] = name
            items['year'] = row.xpath('.//td[1]/text()').get()
            items['population'] = row.xpath('.//td[2]/strong/text()').get()
            items['yearly_change_percent'] = row.xpath('.//td[3]/text()').get()
            items['yearly_change'] = row.xpath('.//td[4]/text()').get()
            items['net_migrants'] = row.xpath('.//td[5]/text()').get()
            items['median_age'] = row.xpath('.//td[6]/text()').get()
            items['fertility_rate'] = row.xpath('.//td[7]/text()').get()
            items['density_per_kmsq'] = row.xpath('.//td[8]/text()').get()
            items['urban_population_percent'] = row.xpath('.//td[9]/text()').get()
            items['urban_population'] = row.xpath('.//td[10]/text()').get()
            items['world_population_share'] = row.xpath('.//td[11]/text()').get()
            items['world_population'] = row.xpath('.//td[12]/text()').get()
            items['global_rank'] = row.xpath('.//td[13]/text()').get()

            yield items
