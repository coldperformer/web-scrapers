import scrapy
import logging
from scrapy.utils.project import get_project_settings

class PopulationbycountrySpider(scrapy.Spider):
    name = 'populationbycountry'
    allowed_domains = ['www.worldometers.info']
    
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

        logging.info(msg=response.status)
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')

        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()
            yearly_change_percent = row.xpath('.//td[3]/text()').get()
            yearly_change = row.xpath('.//td[4]/text()').get()
            net_migrants = row.xpath('.//td[5]/text()').get()
            median_age = row.xpath('.//td[6]/text()').get()
            fertility_rate = row.xpath('.//td[7]/text()').get()
            density_per_kmsq = row.xpath('.//td[8]/text()').get()
            urban_population_percent = row.xpath('.//td[9]/text()').get()
            urban_population = row.xpath('.//td[10]/text()').get()
            world_population_share = row.xpath('.//td[11]/text()').get()
            world_population = row.xpath('.//td[12]/text()').get()
            global_rank = row.xpath('.//td[13]/text()').get()

            yield {
                'country_name': name,
                'year': year,
                'population': population, 
                'yearly_change_percent': yearly_change_percent,
                'yearly_change': yearly_change,
                'migrants(net)': net_migrants,
                'median_age': median_age,
                'fertility_rate': fertility_rate,
                'density_per_kmsq': density_per_kmsq,
                'urban_population_percent': urban_population_percent,
                'urban_population': urban_population,
                'world_population_share': world_population_share,
                'world_population': world_population,
                'global_rank': global_rank,
            }
