# bs4和lxml解析库的使用：主要是用于html网页数据的提取，功能和正则表达式是一样的。

# bs4提取数据是基于css选择器实现的：父子选择器、属性选择器、id选择器、class选择器等。

from bs4 import BeautifulSoup
import requests

# html = requests.get('https://www.baidu.com/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'}).text
#
# #1. 创建bs对象，参数: a> 准备解析的网页源代码；b> 使用的解析器，lxml解析器底层是C语言封装的解析器，解析速度更快；默认有一个Python实现的解析器。将html网页源代码字符串，解析成为一个文档树(DOM)对象。
# bs = BeautifulSoup(html, 'lxml')
# # div#lg：交集选择器，查找id属性='lg'的div标签，两个条件必须同时成立。
# # 选择器>选择器：父子选择器，表示要查找div标签下的class=index-logo-src子标签
# img = bs.select('div#lg > .index-logo-src')[0]
# print(type(img))
#
# # 获取img图片的地址
# url = img.get('src')
# print(url)
#
# all_a = bs.select('div#u1 > a.mnav')
# for a in all_a:
#     # a.text: 获取标签内部的文本值
#     print(a.get('href'), a.text)

# .string和.text的区别
html = """
<a class="one" href="xxx">百度一下</a>
<a class="two" href="==="><p>111</p>a标签内部的内容。<img src="---"></a>
"""
bs = BeautifulSoup(html, 'lxml')
# 情况一：如果一个标签内部只包含文本字符串，不包含子标签，那么使用.string和.text都可以获取标签内部的文本内容。
# a1 = bs.select_one('a.one')
# print('string = ', a1.string)
# print('text = ', a1.text)

# 情况二：如果一个标签内部既有文本，又有其它标签，使用.string就无法获取到数据了，可以使用.text或者.contents获取。
a1 = bs.select_one('a.two')
print('string = ', a1.string)
print('text = ', a1.text)
print('str = ', a1.contents)