# 爬取糗事百科信息。

# 注意：爬取任何一个网站，首先要确定的就是这个网站是静态网站还是动态网站。其次看看这个GET请求是否携带了特殊的参数。最后需要留意请求头中的Cookie信息。

import sqlite3, re
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

class DataTool(object):
    """
    工具类：对提取的元组中的数据，进行整理，删除无效的字符(\n，<br/>)
    """
    # 定义删除\n字符的正则表达式
    pattern_n = re.compile(r'\n', re.S)
    # 定义删除<br/>字符的正则表达式
    pattern_br = re.compile(r'<br/>', re.S)

    def process_tuple_data(self, origin_tuple_data):
        """
        用于对提取的原始元组进行数据处理的函数
        :param origin_tuple_data: 原始数据元组
        :return: 返回整理之后的元组
        """
        # 需要处理的数据：用户昵称、段子内容
        # sub()是正则表达式中的替换数据的方法，需要将\n这个字符替换成空字符
        # 参数：1. 替换规则 2. 替换结果 3. 要匹配的字符串
        nick_name = re.sub(self.pattern_n, '', origin_tuple_data[0])

        # 处理段子内容
        content = re.sub(self.pattern_n, '', origin_tuple_data[2])
        content = re.sub(self.pattern_br, '', content)

        # 将处理后的数据再封装成一个元组，返回
        data = (nick_name, origin_tuple_data[1], content, origin_tuple_data[3], origin_tuple_data[4])
        return data

class DBTool(object):
    """
    将数据保存到数据库中的工具类，主要负责数据库的增删改查操作。
    """
    connect = None
    cursor = None
    # 操作数据库：1.创建数据库的连接对象，创建游标，这两个对象一般连接一次即可；2.数据的增删改查；3.关闭数据库对象、关闭游标对象，一般都是在数据保存完毕之后关闭即可。
    @classmethod
    def create_db_cursor(cls):
        cls.connect = sqlite3.connect('qsbk.db')
        cls.cursor = cls.connect.cursor()

    @classmethod
    def insert_sql(cls, tuple_data):
        """
        执行数据插入sql语句的函数
        :param tuple_data: 使用DataTool工具类整理过后的数据。
        :return:
        """
        sql_str = 'INSERT INTO qs (nick_name, level, content, vote_number, comment_number) VALUES ("%s", "%s", "%s", "%s", "%s")' % (tuple_data[0], tuple_data[1], tuple_data[2], tuple_data[3],tuple_data[4])
        # 开始执行sql语句
        cls.cursor.execute(sql_str)
        cls.connect.commit()

    @classmethod
    def close_db_cursor(cls):
        cls.cursor.close()
        cls.connect.close()

class QSBKSpider(object):
    """
    爬虫类
    """
    def __init__(self):
        # 将各个页面通用的路径，不变的路径声明称为属性，调用方便，直接在这个属性的后面拼接页码。
        self.base_url = 'https://www.qiushibaike.com/hot/page/'
        # 初始化请求头，伪造浏览器请求头中的User-Agent字段值，如果不修改User-Agent字段值，有一个默认的值User-Agent: python-3.7 xxx。
        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'
        # }
        # 实例化工具类DataTool的对象
        self.tool = DataTool()
        # 实例化ua对象
        self.ua = UserAgent()

    def get_list_html(self, page_num):
        """
        获取每一个列表页的html网页源代码(这个获取的源代码就是 "右键-网页源代码" 中的内容)
        page_num：表示将要请求的页面的页码。
        :return:
        """
        # 构造每一页的url地址
        page_url = self.base_url + str(page_num)
        # 向page_url发送GET请求，开始获取当前页page_num的网页源代码
        # 先构造Request请求对象
        headers = {
            # random属性：从ie、firefox、chrome等浏览器的ua中，随机获取一个ua。
            'User-Agent': self.ua.random
        }
        request = Request(page_url, headers=headers)
        try:
            response = urlopen(request)
        except Exception as e:
            print('请求失败：地址{}，原因{}'.format(page_url, e))
            return None
        else:
            # try语句中的请求没有出现异常，就会执行else语句，如果出现异常了就不会执行else语句了。
            # print(response)
            html = response.read().decode()
            return html

    def parse_list_html(self, html):
        """
        解析上一个函数请求的html源代码
        :param html: 请求成功返回列表页的网页源代码，请求失败返回None
        :return:
        """
        if html:
            # 使用正则表达式开始解析网页源代码
            # 写正则注意事项：
            # 1. 尽量找到要匹配的零散数据所在的标签，而且这个标签必须和这些零散的数据一样能够循环。因为findall()函数在循环匹配数据的时候，是按照整个正则表达式规则循环匹配的。
            # 2. 在参考网页中 "审查元素" 来设置正则匹配规则的时候，一定要确认是否和 "网页源代码" 中的标签顺序、属性顺序等保持一致，如果不一致的话，必须参考 "网页源代码" 来设置正则匹配规则。因为 "审查元素" 中的Html代码是经过JS渲染之后的源代码。
            pattern = re.compile(r'<div class="article block.*?>.*?<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
            results_list = re.findall(pattern, html)
            for data in results_list:
                new_data = self.tool.process_tuple_data(data)
                DBTool.insert_sql(new_data)
        else:
            print('html源代码为None')


if __name__ == '__main__':
    # 创建数据库对象、游标对象
    DBTool.create_db_cursor()

    obj = QSBKSpider()

    # 循环爬取多页数据。
    for x in range(1, 10):
        # range()取1到10之间的整数，能取到1，无法取到10
        html = obj.get_list_html(x)
        obj.parse_list_html(html)

    # 关闭数据库、游标对象
    DBTool.close_db_cursor()

# fake_user_agent：pip install fake-useragent 这个第三方库，它维护了各种主流浏览器的UA标识，并且会定期的更新这个库，淘汰一些过期的UA。

