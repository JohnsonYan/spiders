# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from scrapy import log
from scrapy.exceptions import DropItem

#class StackoverflowPipeline(object):
#    def process_item(self, item, spider):
#        return item

class MongoDBPipeline(object):
    # that is the name of MongoDB Collection
    collection_name = 'questions'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.db[self.collection_name].insert(dict(item))
            log.msg("Question added to MongoDB database!", level=log.DEBUG, spider=spider)

        return item
