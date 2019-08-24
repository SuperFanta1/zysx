# 使用多进程对街拍图片进行下载，并将图片相关信息保存到mongodb数据库中。
import requests, re, json, pymongo
from multiprocessing import Pool
from urllib.parse import urlencode
from hashlib import md5
from django.views import View

class JiePaiSpider(object):
    # 进程池无法序列化pymongo对象，因为pymongo数据库中含有线程锁。
    # TypeError: can't pickle _thread.lock objects
    # 建立pymongo的链接
    client = pymongo.MongoClient('localhost')
    db = client['jiepai']

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'
        }

    def get_list_json(self, offset):
        """
        请求列表页的json接口，获取列表页中的图片信息。
        :param offset: 请求接口时的偏移量参数。(0, 20, 40....)
        :return:
        """
        # https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis
        # 准备接口参数
        params = {
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis'
        }
        api_url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
        try:
            response = requests.get(api_url, headers=self.headers)
            if response.status_code == 200:
                # 响应状态码是200，说明GET请求成功
                return response.text
            else:
                print('请求异常：url={}, status_code={}'.format(api_url, response.status_code))
                return None
        except Exception as e:
            print('请求异常：url={}, error={}'.format(api_url, e))
            return None

    def parse_list_json(self, json_str):
        """
        解析列表页json数据
        :param json_str:
        :return:
        """
        json_dict = json.loads(json_str)
        if 'data' in json_dict.keys():
            # 判断字典json_dict的所有键中是否包含'data'，如果有，可以解析，如果没有，可能没有数据或者发生异常了。
            data_list = json_dict.get('data', None)
            if data_list and len(data_list) > 0:
                # 说明还有数据，可以解析
                urls = []
                for item in data_list:
                    if 'single_mode' not in item and 'cell_type' not in item:
                        article_url = item['article_url']
                        urls.append(article_url)
                return urls

    def get_detail_page(self, detail_url):
        try:
            response = requests.get(detail_url, headers=self.headers)
            if response.status_code == 200:
                # 响应状态码是200，说明GET请求成功
                return response.text
            else:
                print('请求异常：url={}, status_code={}'.format(detail_url, response.status_code))
                return None
        except Exception as e:
            print('请求异常：url={}, error={}'.format(detail_url, e))
            return None

    def parse_detail_page(self, detail_html):
        # \(：表示对正则表达式中的(进行转义，转化为一个普通的字符。
        js_json_str = re.findall(re.compile(r'gallery: JSON\.parse\((.*?)\),', re.S), detail_html)[0].replace('\\', '').strip('"')
        # 数据保存到Mongo中
        data_dict = json.loads(js_json_str)
        self.save_dict_to_db(data_dict)

        # 解析Json，取出图片的url地址，下载图片到本地。
        for item_dict in data_dict['sub_images']:
            img_url = item_dict['url']
            # 根据图片url地址，下载图片
            self.download_image(img_url)

    def download_image(self, img_url):
        response = requests.get(img_url, headers=self.headers)
        if response.status_code == 200:
            # response.text: 获取的是文本资源；(json字符串、网页源代码)
            # 但是图片属于二进制资源，图片数据的传输是以二进制流的形式传输的，不再是字符串了。
            content = response.content
            # md5()函数的参数需要是一个bytes字节码，不能是str类型的字符串。
            # hexdigest(): 获取md5加密后的结果。
            img_name = md5(img_url.encode('utf-8')).hexdigest()

            # 'w': 写入普通文本；'wb': 专门用于写入二进制数据(图片、音频、视频)
            f = open('imgs/{}.jpg'.format(img_name), 'wb')
            f.write(content)
            f.close()
        else:
            print('图片请求失败：{}'.format(img_url))

    def save_dict_to_db(self, dic):
        self.db['img'].insert_one(dic)

    def start_spider(self, offset):
        print('正在请求偏移量为{}的图片'.format(offset))
        json_str = self.get_list_json(offset)
        if json_str:
            urls = self.parse_list_json(json_str)
            for detail_url in urls:
                detail_html = self.get_detail_page(detail_url)
                if detail_html:
                    self.parse_detail_page(detail_html)

if __name__ == '__main__':
    jp = JiePaiSpider()
    pool = Pool(3)
    pool.map(jp.start_spider, [x for x in range(0, 101) if x % 20 == 0])
    # jp.start_spider(0)
    pool.close()
    pool.join()

# 预习：bs4和xpath。

