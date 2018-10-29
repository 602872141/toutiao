# -*- coding: utf-8 -*-
import hashlib

import scrapy
from scrapy import Request
from fake_useragent import UserAgent
import json
import re
from PIL import Image
from io import BytesIO

from toutiao.items import ToutiaoItem


class BizhiSpider(scrapy.Spider):
    name = 'bizhi'
    allowed_domains = ['ic.snssdk.com']
    start_urls = ['http://ic.snssdk.com/']
    url='https://is.snssdk.com/api/feed/profile/v1/?category=profile_article&visited_uid=92376431372&stream_api_version=88&count=20&offset={offset}&iid=44419958674&device_id=47486856279&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=691&version_name=6.9.1&device_platform=android&ab_version=271178%2C424179%2C326524%2C326532%2C496389%2C345191%2C519951%2C518640%2C515800%2C504724%2C469022%2C510933%2C455644%2C493567%2C424176%2C214069%2C520850%2C510710%2C442255%2C519258%2C521871%2C512958%2C489509%2C280447%2C521245%2C281296%2C513401%2C325617%2C521558%2C509889%2C506003%2C520553%2C386892%2C498375%2C516131%2C467513%2C515673%2C516097%2C444464%2C425531%2C511489%2C512528%2C507360%2C341308%2C486953%2C475404%2C494120%2C239096%2C500091%2C170988%2C493249%2C519890%2C374116%2C495949%2C478529%2C517767%2C489313%2C501960%2C276205%2C459646%2C459996%2C515935%2C500386%2C517536%2C416055%2C510640%2C517324%2C392460%2C378450%2C471407%2C510757%2C519795%2C518782%2C509308%2C512914%2C261580%2C519914%2C403271%2C293032%2C457480%2C502679%2C510536&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=Mi+Note+3&device_brand=Xiaomi&language=zh&os_api=27&os_version=8.1.0&uuid=865499035399441&openudid=73dbaeddd4b81bd4&manifest_version_code=691&resolution=1080*1920&dpi=440&update_version_code=69111&_rticket=1538105841731&plugin=26958&pos=5r_-9Onkv6e_v7G_8fLz-vTp6Pn4v6esrK6zqayrqamtpK6xv_H86fTp6Pn4v6evrrOsqqytqauuqLG__PD87d706eS_p794JCJ4KgN4JR-_sb_88Pzt0fLz-vTp6Pn4v6esrK6zqa-sqK6ssb_88Pzt0fzp9Ono-fi_p6-us6yrpampquA%3D&fp=2rTqLMmSc2P_FlcWPrU1FlxScrq_&tma_jssdk_version=1.2.2.4&rom_version=miui_v10_v10.0.2.0.ochcnfh&ts=1538105842&as=a2750abac25fab811d1357&mas=00d173d1c0b8b877d48ff93a92af6de64c454ce6e60c682e64'
    ua = UserAgent()

    def get_headers(self):

        headers = {
            'Host': 'ic.snssdk.com',
            'Upgrade - Insecure - Requests': '1',
            'User - Agent': self.ua.random
        }
        return headers
    def start_requests(self):
        url=self.url.format(offset='0')
        print(url)
        headers = self.get_headers()
        
        yield Request(url=url,callback=self.parse,headers=headers)
    
    def parse(self, response):
        result = json.loads(response.text)

        print('开始')
        headers = self.get_headers()

        if result.get('data'):
            item = ToutiaoItem()
            list=[]
            for content in result.get('data'):

                get = content

                re_compile = re.compile('"Abstract":"(.*?)","abstract"')
                match = re.findall(re_compile, str(get))
                if match[0].find('壁纸')!=-1:
                    re_compile = re.compile(
                        '.*?"url_list":.{"url":"(http://sf\d-ttcdn-tos.pstatp.com/img/pgc-image/.*?~400x400_c5.webp)"},{"url":"')
                    findall = re.findall(re_compile, str(get))
                    #1. 一张一张下
                    # if len(findall)<=4:
                    #     for url in findall:
                    #         item['name']=match[0]
                    #         item['img_url'] =url
                    #         yield item
                #     2. 一篇一篇下
                    if len(findall) <= 4:
                        item['name'] = match[0]
                        item['img_url'] = findall
                        yield item
                # list.append(findall)
            # item['img_url'] = list
            #     item['img_url'] = findall
            #     yield item
            offset = result.get('offset')
            yield Request(url=self.url.format(offset=offset), callback=self.parse, headers=headers,dont_filter= True)
            # yield  Request(url="https://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537196767030d5004e9eec~400x400_c5.webp",callback=self.xiazai_parse,dont_filter=True)

    def get_md5(url):

        if isinstance(url, str):
            url = url.encode("utf-8")
        m = hashlib.md5()
        m.update(url)
        return m.hexdigest()


