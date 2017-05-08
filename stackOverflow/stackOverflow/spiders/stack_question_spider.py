#!/usr/bin/env python3
#coding=utf-8

import scrapy
from stackOverflow.items import QuestionItem

class QuestionSpider(scrapy.Spider):
    # spider name
    name = "question"
    # only scrape domain in allowed_domains
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?page=1&sort=newest"
    ]

    def parse(self, response):
        for question in response.xpath('//div[@class="summary"]/h3'):
            item = QuestionItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract_first()
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract_first()
            yield item

        for i in range(1,11):
            next_page = "http://stackoverflow.com/questions?page=%s&sort=newest" % str(i)
            yield scrapy.Request(next_page, callback=self.parse)

