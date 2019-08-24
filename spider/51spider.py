# 讲解51job(前程无忧)网站数据
from urllib.request import urlopen, Request, urlretrieve
import re, json

def parse_city_code():
    """
    请求并解析城市编码的函数
    :return: 返回一个字典
    """
    # decode()函数默认使用utf8转化字节码，但是51job网页采用的是gbk编码(右键-网页源代码：<meta http-equiv="Content-Type" content="text/html; charset=gbk">，charset属性就是用来设置网页的编码方式的)，所以需要使用decode('gbk')将bytes转化成str类型。
    js_content = urlopen('https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20180319').read().decode('gbk')
    # 1. 先利用 '=' 字符对这个字符串进行切割split() -> 返回列表
    str_list = js_content.split('=')
    # 2. 切割之后，'='左边的内容是列表中的第一个元素，'='右边的是第二个元素
    # replace(';', ''): 将字符串中的 ';' 字符，替换成空字符。
    str_dict = str_list[1].replace(';', '')
    # 3. 将这个json字符串，转化为Python中的字典。
    # loads()：将json字符串 -> dict
    # dumps()：将dict -> json字符串
    dic = json.loads(str_dict)

    # 4. 将dic这个字典中的键值对互换位置，因为用户输入的是城市名称，程序需要根据城市名称获取对应的编码，所以将城市名称作为键，城市编码作为值。
    new_dict = {}
    for key, value in dic.items():
        new_dict[value] = key

    return new_dict

class JOB51Spider(object):
    """
    爬虫类
    """
    def __init__(self, keyword, citys, city_dict):
        # 该参数是用于获取用户输入的查询城市；
        # self.citys = ['郑州', '北京', '上海']
        # 查询的职位关键字信息；
        # self.keyword = keyword
        # 郑州：170200 北京：010000 上海：020000
        # https://search.51job.com/list/170200%252C010000%252C020000,000000,0000,00,9,99,Python,2,10.html
        city_code = ''
        for key in citys:
            city_code += city_dict[key]
            if key != citys[-1]:
                # 如果遍历出来的key的值，不等于列表中最后一个元素的值，那么在这个城市编码后面添加'%252C'
                city_code += '%252C'
        self.base_url = 'https://search.51job.com/list/' + city_code + ',000000,0000,00,9,99,' + keyword + ',2,{}.html'

    def get_list_html(self, page_num=1):
        """
        请求列表页url，获取网页源代码
        :param page_num: 当前页的页码
        :return: 返回网页源代码，交给下一个函数进行解析
        """

        list_url = self.base_url.format(page_num)
        try:
            html = urlopen(list_url).read().decode('gbk')
        except Exception as e:
            print('列表页请求异常：url={}, error={}'.format(list_url, e))
            return None
        else:
            return html

    def get_total_page_num(self):
        """
        获取搜索结果的总页数
        :return:
        """
        html = urlopen(self.base_url.format(1)).read().decode('gbk')
        total_num_pattern = re.compile(r'<span class="td">共(.*?)页', re.S)
        total_num = int(re.findall(total_num_pattern, html)[0])
        return total_num

    def parse_list_html(self, list_html):
        """
        解析列表页源代码，提取每一个职位的详情页地址。
        :param list_html: 列表页源代码
        :return:
        """
        detail_url_pattern = re.compile(r'<div class="el">.*?<p class="t1 ">.*?<a.*?href="(.*?)".*?>', re.S)
        detail_url = re.findall(detail_url_pattern, list_html)
        return detail_url

    def get_detail_html(self, detail_url):
        """
        请求详情页函数
        :param detail_url:
        :return: 返回详情页的源代码，交给下一个函数提取详情页的数据。
        """
        try:
            html = urlopen(detail_url).read().decode('gbk')
        except Exception as e:
            print('详情页请求异常：url={}, error={}'.format(detail_url, e))
            return None
        else:
            return html, detail_url

    def parse_detail_html(self, detail_html, detail_url):
        """
        提取详情页数据
        :param detail_html:
        :return:
        """
        if 'jobs.51job.com' in detail_url:
            # 大众化的页面结构
            pattern = re.compile(r'<div class="cn">.*?<h1 title="(.*?)">.*?<strong>(.*?)</strong>.*?<p class="cname">.*?<a.*?title="(.*?)".*?>.*?<p.*?title="(.*?)".*?>.*?<div class="t1">(.*?)</div>', re.S)
            results = re.findall(pattern, detail_html)[0]
            print(results)
        elif '51rz.51job.com' in detail_url:
            print('51rz.51job.com: ', detail_url)
        else:
            print('其它URL：', detail_url)


if __name__ == '__main__':
    city_dict = parse_city_code()
    citys = input('请输入查询城市名称(多个城市使用,号隔开)：')
    # if ',' in citys:
    #     # 多个城市
    #     city_list = citys.split(',')
    # else:
    #     # 一个城市
    #     city_list = [citys]

    # 如果if ',' in citys:条件成立，采用if前面的值citys.split(','); 如果if条件不成立，采用else后面的值[citys]；
    city_list = citys.split(',') if ',' in citys else [citys]
    kw = input('请输入职位关键字：')
    obj = JOB51Spider(keyword=kw, citys=city_list, city_dict=city_dict)
    total_num = obj.get_total_page_num()
    for number in range(1, total_num):
        print('开始获取第{}页数据...'.format(number))
        list_html = obj.get_list_html(number)
        detail_urls = obj.parse_list_html(list_html)
        for detail_url in detail_urls:
            # 将detail_url交给下一个函数去请求。
            detail_html, url = obj.get_detail_html(detail_url)
            obj.parse_detail_html(detail_html, url)
