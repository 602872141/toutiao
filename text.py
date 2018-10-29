import json
import re
import requests
from PIL import Image, ImageEnhance
from io import BytesIO

from pytesseract import pytesseract, image_to_string
from selenium.common.exceptions import TimeoutException

test='"{"Abstract":"高清无水印壁纸:意境，唯美，简洁，风景，可爱鸭，动漫等","abstract":"","action_extra":"","action_list":null,"activity":null,"ad_button":null,"aggr_type":2,"allow_download":false,"article_alt_url":"","article_open_url":null,"article_sub_type":0,"article_type":0,"article_url":"http://toutiao.com/group/6601489349064262148/","ban_bury":0,"ban_comment":false,"ban_danmaku":null,"ban_digg":0,"behot_time":1537029014,"bury_count":0,"cell_ctrls":{"cell_flag":5898240,"cell_height":0,"cell_layout_style":26,"content_decoration":null,"need_client_impr_recycle":null},"cell_flag":5898240,"cell_layout_style":26,"cell_type":0,"cell_ui_type":null,"city":"","cold_start":null,"comment":null,"comment_count":1,"commoditys":null,"content_decoration":null,"cursor":0,"danmaku_count":null,"data_type":1,"debug_info":null,"detail_mode":null,"digg_count":0,"disallow_web_transform":null,"display_url":"http://toutiao.com/group/6601489349064262148/","entity_info":null,"filter_words":null,"follow_button_style":0,"forward_info":{"forward_count":1},"gallary_flag":null,"gallary_image_count":0,"gallary_style":null,"group_flags":2,"group_id":6601489349064262148,"group_source":2,"group_type":0,"has_audio":null,"has_image":true,"has_m3u8_video":false,"has_mp4_video":false,"has_video":false,"hot":0,"id":6601489349064262148,"ignore_web_transform":0,"image_list":[{"height":400,"uri":"pgc-image/1537028954309acfef708cc","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/1537028954633624ee67c3f","url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~400x400_c5.webp","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~400x400_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/153702895530381607c8c77","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/153702895580001ab4c015c","url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~400x400_c5.webp","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~400x400_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/1537028956463cfb91af0a5","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/1537028956649f9fb847c53","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/1537028956428450ee44ecb","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/153702895664730ee4b558f","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~400x400_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~400x400_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~400x400_c5.webp"}],"width":400},{"height":400,"uri":"pgc-image/153702895678905d872a547","url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~400x400_c5.webp","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~400x400_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~400x400_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~400x400_c5.webp"}],"width":400}],"image_type":null,"info_desc":"","interaction_data":null,"is_original":false,"is_subject":false,"is_subscribe":null,"item_id":6601489349064262148,"item_id_str":"6601489349064262148","item_version":0,"keywords":"","label":"","label_extra":null,"label_style":0,"large_image_list":[{"height":380,"uri":"pgc-image/1537028954309acfef708cc","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/1537028954633624ee67c3f","url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~720x380_c5.webp","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~720x380_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028954633624ee67c3f~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/153702895530381607c8c77","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895530381607c8c77~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/153702895580001ab4c015c","url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~720x380_c5.webp","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~720x380_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895580001ab4c015c~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/1537028956463cfb91af0a5","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956463cfb91af0a5~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/1537028956649f9fb847c53","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956649f9fb847c53~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/1537028956428450ee44ecb","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/1537028956428450ee44ecb~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/153702895664730ee4b558f","url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~720x380_c5.webp","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~720x380_c5.webp"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895664730ee4b558f~720x380_c5.webp"}],"width":720},{"height":380,"uri":"pgc-image/153702895678905d872a547","url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~720x380_c5.webp","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~720x380_c5.webp"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~720x380_c5.webp"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/153702895678905d872a547~720x380_c5.webp"}],"width":720}],"level":0,"like_count":0,"log_pb":{"impr_id":"20180926223750010011044228490FEBD"},"media_info":null,"media_name":"","middle_image":{"height":1385,"uri":"list/pgc-image/1537028954309acfef708cc","url":"http://p9.pstatp.com/list/pgc-image/1537028954309acfef708cc","url_list":[{"url":"http://p9.pstatp.com/list/pgc-image/1537028954309acfef708cc"},{"url":"http://pb3.pstatp.com/list/pgc-image/1537028954309acfef708cc"},{"url":"http://p.pstatp.com/list/pgc-image/1537028954309acfef708cc"}],"width":640},"natant_level":0,"need_client_impr_recycle":null,"open_url":null,"outsourcing_id":"","packed_json_str":null,"preload_resource_url":null,"preload_web":0,"publish_time":1537029014,"raw_data":null,"read_count":350,"reason":"","reback_flag":0,"recommend_label":null,"recommend_reason":null,"recommond_reason":null,"repin_count":0,"repin_time":0,"req_id":null,"rid":"20180926223750010011044228490FEBD","search_labels":null,"share_count":0,"share_info":null,"share_type":null,"share_url":"","show_dislike":false,"show_max_line":null,"show_more":null,"show_portrait":null,"show_portrait_article":null,"source":"图文之'
# re_compile = re.compile('.*?"url_list":.{"url":"(http://sf\d-ttcdn-tos.pstatp.com/img/pgc-image/.*?~400x400_c5.webp)"},{"url":"')
# # findall = re.findall(re_compile, test)
# #
# #
# #
# #
# #
# # response = requests.get('http://sf1-ttcdn-tos.pstatp.com/img/pgc-image/1537028954309acfef708cc~400x400_c5.webp')
# # image = Image.open(BytesIO(response.content))
# # uri='image'
# # image.save(uri+'\ww.jpg')
# list=[1,25,4,9,4,8]
# print(type(list)=='List')
# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from PIL import Image
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from io import BytesIO
# import pytesseract
#
# browser = webdriver.Chrome()
# browser.get('https://sso.toutiao.com/')
# wait = WebDriverWait(browser, 20)
# wait.until(EC.element_to_be_clickable(
#             (By.CSS_SELECTOR, "body > div > div > div.loginBox > div > div > div > ul > li.sns.mail-login"))).click()
# try:
#     img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div.loginBox > div > div > div > form > div.input-field.verification > div > img')))
# except TimeoutException:
#     print('未出现验证码')
# screenImg=r'D:\Python_data\toutiao\01.png'
# screenImg2=r'D:\Python_data\toutiao\02.png'
#
# browser.get_screenshot_as_file(screenImg)
# im=Image.open(screenImg)
#
# location = img.location
# size = img.size
# top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
#     'width']
# region = im.crop((left,top,right,bottom))
#
# region.save(screenImg)
#
# img = Image.open(screenImg)
# img = img.convert('L')
# img = ImageEnhance.Contrast(img)
# img = img.enhance(2.0)
#
# img.save(screenImg2)
#
# img = Image.open(screenImg2)
# # print(img)
# # code =image_to_string(img)
# # code = pytesseract.image_to_string(img)
# img.show()
# s = input('验证码')
# Username = wait.until(EC.presence_of_element_located((By.ID, 'account')))
# Password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
# yanzheng = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#captcha")))
# submit = wait.until(EC.element_to_be_clickable((By.NAME, 'submitBtn')))
#
# Username.send_keys('17328629738')
# Password.send_keys('qQ602872141')
# yanzheng.send_keys(s)
#
# submit.click()
#
# cookies = browser.get_cookies()
# dict = {}
# for cookie in cookies:
#     dict[cookie['name']] = cookie['value']
#
# print(dict)
#
url='https://is.snssdk.com/api/feed/profile/v1/?category=profile_article&visited_uid=92376431372&stream_api_version=88&count=20&offset=0&iid=45228606282&device_id=47486856279&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=692&version_name=6.9.2&device_platform=android&ab_version=425531%2C511489%2C512528%2C507360%2C341308%2C486953%2C475404%2C494120%2C519224%2C523908%2C239096%2C500091%2C170988%2C493249%2C523533%2C374116%2C495949%2C478529%2C517767%2C489313%2C501960%2C276205%2C459646%2C459996%2C515935%2C521045%2C500386%2C517536%2C416055%2C510640%2C517324%2C392460%2C378450%2C471407%2C522906%2C519795%2C523156%2C518782%2C509308%2C512914%2C271178%2C424179%2C326524%2C523980%2C326532%2C524855%2C496389%2C345191%2C519951%2C518640%2C504724%2C469022%2C510933%2C455644%2C493567%2C525310%2C424176%2C214069%2C524820%2C524910%2C442255%2C519258%2C522212%2C489509%2C280447%2C523499%2C281296%2C513401%2C325617%2C524586%2C525837%2C523143%2C506003%2C520553%2C386892%2C498375%2C521931%2C467513%2C515673%2C516097%2C444464%2C261580%2C519914%2C403271%2C293032%2C457480%2C502679%2C510536%2C523059&ab_client=a1%2Cc4%2Ce1%2Cf1%2Cg2%2Cf7&ab_feature=94563%2C102749&abflag=3&ssmix=a&device_type=Mi+Note+3&device_brand=Xiaomi&language=zh&os_api=27&os_version=8.1.0&uuid=865499035399441&openudid=73dbaeddd4b81bd4&manifest_version_code=692&resolution=1080*1920&dpi=440&update_version_code=69210&_rticket=1538288821354&plugin=26958&pos=5r_x8vP69Ono-fi_p6ysqLOvramrqK6kpK6uqaulqrG_8fzp9Ono-fi_p6-vs6Wlqqilrq6qqqqlq62pqrG__PD87d706eS_p797LAh4LSN4JR-_sb_88Pzt0fLz-vTp6Pn4v6esrKizr62krqWusb_88Pzt0fzp9Ono-fi_p6-vs6WlqK-qquA%3D&fp=2rTqLMmSc2P_FlcWPrU1FlxScrq_&tma_jssdk_version=1.2.2.4&rom_version=miui_v10_v10.0.2.0.ochcnfh&ts=1538288821&as=a2b5764b25fb9b4cd05273&mas=003e433855bcf936491c388261678aecea0c4266648e200af4'
response = requests.get( 'http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/15381326103742bc568d7e3~400x400_c5.webp')
if response.status_code==200:
    print(response.text)
    # loads = json.loads(response.text)
    # loads_get = loads.get('data')
    # print(loads_get[0])
    # re_compile = re.compile('"Abstract":"(.*?)","abstract"')
    # match = re.findall(re_compile, loads_get[0])
    # print(match[0].find('壁纸'))