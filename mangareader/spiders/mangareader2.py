# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request
from mangareader.items import MangareaderItem


class Mangareader2Spider(CrawlSpider):
    name = 'mangareader2'
    allowed_domains = ['mangareader.net']
    start_urls = ['http://www.mangareader.net/']

    rules = (
        Rule(LinkExtractor(allow=r'alphabetical'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #i = MangareaderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        print "book_list_url"
        sel = Selector(response)
        url = sel.xpath('//*[@class="series_alpha"]/li/a/@href').extract()

        for urllist in url:
            yield Request('http://www.mangareader.net'+urllist, callback=self.book_url)

    
    def book_url(self, response):
        """
        The book  infomation
        """
        #print "book_url"
        items = []
        i = MangareaderItem()
        sel = Selector(response)
        i['name'] = sel.xpath('//*[@class="aname"]/text()').extract()
        i['Alternate_Name'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[2]/td[2]/text()').extract()
        i['Year_of_Release'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[3]/td[2]/text()').extract()
        i['Status'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[4]/td[2]/text()').extract()
        i['Author'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[5]/td[2]/text()').extract()
        i['Artist'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[6]/td[2]/text()').extract()
        i['Reading_Direction'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[7]/td[2]/text()').extract()
        i['Genre'] = sel.xpath('//*[@id="mangaproperties"]/table/tr[8]/td[2]/a/span/text()').extract()
        i['readmangasum'] = sel.xpath('//*[@id="readmangasum"]/p/text()').extract()
        i['image_urls'] = sel.xpath('//*[@id="mangaimg"]/img/@src').extract()

        items.append(i)
        return items


