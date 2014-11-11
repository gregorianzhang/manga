# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.item import Item, Field


class MangareaderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
	
	name = Field()
	Alternate_Name = Field()
	Year_of_Release = Field()
	Status = Field()
	Author = Field()
	Artist = Field()
	Reading_Direction = Field()
	Genre = Field()
	readmangasum = Field()
	images = Field()
	image_urls = Field()
	image_paths = Field()

