# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json

from scrapy import signals
import requests


class ToutiaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ToutiaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
# class proxy_Middleware(object):
#
#     def get_proxy(self):
#         try:
#             response = requests.get('http://localhost:5555/random')
#             if response.status_code == 200:
#                 return response.text
#         except requests.ConnectionError:
#             return False
#     def process_request(self, request, spider):
#         proxy = self.get_proxy()
#
#         if proxy:
#             print("----------------{0}-----------------------".format(proxy))
#             uri='https://{proxy}'.format(proxy=proxy)
#             request.meta['proxy']=uri

class cookies_Middleware(object):

    # def get_cookies(self):
    #     response = requests.get('http://localhost:5000/toutiao/random')
    #     if response.status_code == 200 :
    #         cookies = json.loads(response.text)
    #
    #     return cookies

    def get_random_cookies(self):
        response = requests.get('http://localhost:5000/toutiao/random')
        if response.status_code == 200:
            cookies = json.loads(response.text)
            return cookies
    def process_request(self, request, spider):
        # if request.flags:
        #     if request.flags[0] == 1:
        #         return None
            request.cookies=self.get_random_cookies()

            return None

    # def process_response(self, request, response, spider):
    #
    #     if response.status in [302, 301]:
    #         redirect_url = response.headers['location']
    #         if 'passport' in redirect_url:
    #             self.logging.info('Cookies Invaild!')
    #         if '验证页面' in redirect_url:
    #             self.logging.info('当前Cookie无法使用，需要认证。')
    #         request.cookies = self.get_random_cookies()
    #         return request
    #     return response


import base64

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "H3H8F98372H71X8D"
proxyPass = "CF747EB70C0404DB"

# for Python2
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


# for Python3
# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        request.headers["Proxy-Authorization"] = proxyAuth
