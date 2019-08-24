# lxml用法：xpath路径提取数据，也支持css选择器的写法。

# etree: element tree文档树，将html源代码转化为一个文档树对象。
from lxml.html import etree

html = """
<a class="one" id="first" href="xxx">百度一下</a>
<a class="two three four" href="==="><p>111</p>a标签内部的内容。<img src="---"></a>
<div>
    <span>五险一金</span>
    <span>双休</span>
    <span>餐补</span>
</div>
"""
# parser: 解析器。
obj = etree.HTML(html, parser=etree.HTMLParser(encoding='utf8'))
# <class 'lxml.etree._Element'>
print(type(obj))
# a[@class="one"]：查找class="one"的a标签，[@class="xx"]固定用法
# //：表示从html源码中的任意位置查找标签。
# 提取标签属性的写法
# /@href /@src /@id /@class
content = obj.xpath('//a[@class="one"]/@href')
print(content)

# 提取标签的文本内容的写法
text = obj.xpath('//a[@class="one"]/text()')
print(text)

# 如果要提取一个标签的属性和文本等多个内容，一般都不采用上面这种写法，xpath路径重复的内容太多。先定位到标签，然后再单独从这个标签中提取需要的内容
a = obj.xpath('//a[@class="one"]')[0]
# <class 'lxml.etree._Element'>: 只有对象是该类型_Element的，才能调用xpath()方法。
print(type(a))
print(a.xpath('@href'), a.xpath('text()'))

# //a[@class="two"]/img: /img表示在a标签的基础上，查找a标签的子标签img。
# src = obj.xpath('//a[@class="two"]/img/@src')[0]
# print(src)

src = obj.xpath('//a[@class="two three four"]/img/@src')[0]
print(src)

# 如果标签class属性有多个值，为了xpath语法简介，可以使用contains()
s1 = obj.xpath('//a[contains(@class, "three")]/img/@src')[0]
print(s1)

a1 = obj.xpath('//a[@id="first"]/text()')[0]
print(a1)

# //text()：表示提取div标签下的所有标签的文本内容。
texts = obj.xpath('//div//text()')
res = ';'.join([s for s in texts if '\n' not in s])
print(res)

# 利用标签的位置定位标签：找到div标签下的第一个span标签。
span = obj.xpath('//div/span[1]/text()')[0]
print(span)

