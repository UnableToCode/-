# -*- coding: utf-8 -*-

import logging
import scrapy
from stackoverflow.spiders.items import StackoverflowItem


formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('monitor')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"
    allowed_domains = ["https://stackoverflow.com"]

    def __init__(self):
        self.count = 1

    def start_requests(self):
        _url = 'https://stackoverflow.com/questions/tagged/ide?tab=newest&page={page}&pagesize=50'
        urls = [_url.format(page=page) for page in range(1, 187)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for index in range(1, 51):
            self.count += 1
            if self.count % 100 == 0:
                logger.info(self.count)

            sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
            item = StackoverflowItem()
            # item['votes'] = sel.xpath(
            #     'div[1]/div[2]/div[1]/div[1]/span/strong/text()').extract()
            # item['answers'] = sel.xpath(
            #     'div[1]/div[2]/div[2]/strong/text()').extract()
            # item['views'] = "".join(
            #     sel.xpath('div[1]/div[3]/@title').extract()).split()[0].replace(",", "")
            item['questions'] = sel.xpath('div[2]/h3/a/text()').extract()
            # item['links'] = "".join(
            #     sel.xpath('div[2]/h3/a/@href').extract()).split("/")[2]
            item['tags'] = sel.xpath('div[2]/div[2]/a/text()').extract()
            yield item