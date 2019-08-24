# 爬取人人车车辆信息。
# 多线程/多进程：提高代码的执行效率，放在爬虫中就是提高爬取效率。因为可以使用多个进程同时对多个页面发起请求。
# 之前的糗事百科/51job同步执行：按照先后顺序，一个一个的执行页面请求。

from urllib.request import urlopen
from urllib.error import HTTPError
# 进程池：比较方便，使用简单。
from multiprocessing import Pool

import re, sqlite3

class RRCSpider(object):
    """
    人人车爬虫类
    """
    def __init__(self):
        pass
        # 建立数据库对象和游标对象
        # self.connect = sqlite3.connect('rrc.db')
        # self.cursor = self.connect.cursor()

    def get_list_html(self, page_num):
        """
        获取列表页源代码
        :param page_num: 列表页的页码
        :return: 返回网页源代码
        """
        list_url = 'https://www.renrenche.com/zz/ershouche/p{}/'.format(page_num)
        try:
            list_html = urlopen(list_url).read().decode()
        except HTTPError as e:
            print('列表页异常：url={}, error={}'.format(list_url, e))
            return None, None
        else:
            return list_html, list_url

    def parse_list_html(self, list_html, list_url):
        """
        解析列表页数据
        :param list_html: 列表页网页源代码
        :return: 返回每一个数据的详情页地址
        """
        # 利用正则表达式提取列表页中所有二手车的详情页的链接。
        detail_urls = re.findall(re.compile(r'<li class="span6 list-item.*?".*?<a.*?href="(.*?)".*?class="thumbnail"', re.S), list_html)
        if detail_urls:
            return detail_urls
        else:
            print('列表页数据为空：url={}'.format(list_url))
            return None

    def get_detail_html(self, detail_url):
        """
        获取详情页源代码
        :param detail_url: 详情页的url
        :return: 返回详情页网页源代码
        """
        try:
            detail_html = urlopen(detail_url).read().decode()
        except HTTPError as e:
            print('详情页异常：url={}, error={}'.format(detail_url, e))
            return None, None
        else:
            return detail_html, detail_url

    def parse_detail_html(self, detail_html, detail_url):
        """
        解析详情页数据
        :param detail_html: 详情页网页源代码
        :return: None
        """
        # [('本天', '6.7', '2010')]
        data = re.findall(re.compile(r'<h1 class="title-name rrc.*?">(.*?)</h1>.*?<p class="price.*?">(.*?)</p>.*?<p class="money.*?首付(.*?)<.*?月供(.*?)</p>.*?<ul class=".*?box-list-primary-detail">.*?<strong class="car-summary rrc.*?">(.*?)</strong>.*?<p class="small-title rrc.*?">(.*?)</p>.*?<strong.*?id="car-licensed">(.*?)</strong>.*?<p>.*?<strong class="car-summary">(.*?)</strong>.*?<p class="transfer-record">.*?<strong.*?>(.*?)</strong>', re.S), detail_html)[0]
        print(data)


    def start_spider(self, num):
        """
        爬虫程序启动入口
        :return:
        """
        print('正在请求第{}页'.format(num))
        list_html, list_url = self.get_list_html(num)
        if list_html:
            detail_urls = self.parse_list_html(list_html, list_url)
            if detail_urls:
                for detail_url in detail_urls:
                    url = 'https://www.renrenche.com' + detail_url
                    detail_html, d_url = self.get_detail_html(url)
                    if detail_html:
                        self.parse_detail_html(detail_html, d_url)

if __name__ == '__main__':
    obj = RRCSpider()

    # 这是同步for循环
    # for x in range(1, 2):
    #     obj.start_spider(x)

    # 多进程for循环：第一页、第二页...同时开始获取数据
    # 创建进程池对象，并指定创建进程的数量。
    pool = Pool(3)

    pool.map(obj.start_spider, [x for x in range(1, 11)])

    # 让主进程等待：等待子进程的任务执行完毕以后，再执行主进程的后续代码。
    # 主进程是控制程序的启动和结束，一旦主进程停止，那么整个程序也就终止了。默认情况下，主进程是不会等待子进程的任务执行完毕的，因为进程间的任务执行是相互独立的，所以，如果主进程在子进程任务没有执行完毕的前提下就关闭了主进程，那么子进程剩余的任务就无法执行了，所以，必须让主进程等待子进程，否则任务无法全部执行完毕。
    pool.close()
    pool.join()

    # obj.cursor.close()
    # obj.connect.close()
