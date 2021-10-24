# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorldometersItem(scrapy.Item):
    pass

class PopulationByCountryItem(scrapy.Item):
    
    country = scrapy.Field()
    year = scrapy.Field()
    population = scrapy.Field()
    yearly_change_percent = scrapy.Field()
    yearly_change = scrapy.Field()
    net_migrants = scrapy.Field()
    median_age = scrapy.Field()
    fertility_rate = scrapy.Field()
    density_per_kmsq = scrapy.Field()
    urban_population_percent = scrapy.Field()
    urban_population = scrapy.Field()
    world_population_share = scrapy.Field()
    world_population = scrapy.Field()
    global_rank = scrapy.Field()

class PopulationByYearItem(scrapy.Item):

    year = scrapy.Field()
    world_population = scrapy.Field()
    yearly_change = scrapy.Field()
    net_change = scrapy.Field()
    density_per_kmsq = scrapy.Field()
    urban_pop = scrapy.Field()
    urban_pop_percent = scrapy.Field()