# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from fake_useragent import UserAgent
import pymongo
class ToutiaoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db= self.client[self.mongo_db]


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        self.db['bizhi'].update({'id':item.get('id')},{'$set':item},True)
        return item


# 图片下载
class input_imagePipeline(ImagesPipeline):
    # def get_media_requests(self, item, info):
    #     for image_url in item['img_url']:
    #         # yield Request(image_url,headers=self.get_headers())
    #         if len(image_url)>=2:
    #             if len(image_url)<=3:
    #                 for url in image_url:
    #                     # yield Request(url, headers=self.get_headers(), dont_filter=True)
    #                     yield Request(url, headers=self.get_headers())
    #                 # print(url)
    #
    #                 print('----------------------------------')
    #         else:
    #             print(image_url)
    #             # print('----------------------------------')
    #             # yield Request(image_url,headers=self.get_headers(),dont_filter=True)
    def get_media_requests(self, item, info):
            # 1. 一张一张下
            # item['id']=get_md5(item['img_url'])
            # yield Request(item['img_url'] ,dont_filter=True)
            # print('----------------------------------')
    #     2. 一篇一篇下
        item['id'] = get_md5(item['img_url'][0])
        for url in item['img_url']:

            yield Request(url ,dont_filter=True)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        print(image_paths)
        if not image_paths:
             raise DropItem('Item contains no images')
        item['image_path'] = image_paths
        return item

    def get_headers(self):

        headers = {
            'Host': 'ic.snssdk.com',
            'Upgrade - Insecure - Requests': '1',
            'User - Agent': UserAgent().chrome
        }
        return headers

def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()