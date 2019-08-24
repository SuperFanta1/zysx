# coding: utf-8
# 正则表达式：正则表达式主要是操作字符串的，实现数据的提取，查找和替换。
import re

str1 = '''
123abcd
abc
456
'''
p3 = re.compile(r'123(.*?)456', re.S)
print('======', re.findall(p3, str1))


# re模块提供的方法：match()、search()、findall()、sub()

string = '<a>1</a><a>2</a><a>3</a><a>4</a><a>5</a>'

# 1. 创建正则表达式对象
# r: 主要作用是为了区分python中的转义字符和正则表达式中的转义字符，防止冲突。
# Python的转义字符：\b (退格：删除)
# 正则表达式中的转义字符：\b (匹配字符的两端数据)
# 一般Python的转义字符比较少，而正则表达式中的转义字符很多，如果有冲突的情况需要加r''，没有冲突不需要加r''，都加上r''也没有错。
a = re.compile(r'a\bc', re.S)

# re.S: 因为正则表达式匹配数据的时候是按照行进行匹配的，如果字符串中出现换行了，没有携带re.S，匹配结果就可能不正确。
pattern = re.compile(r'<a>(.*?)</a>', re.S)
# .*和.*?的区别：
# ()表示要提取的数据：凡是需要提取的数据，都需要使用()包起来。

# 2. 根据pattern定义的规则，去string这个字符串中匹配数据。
results = re.findall(pattern, string)
print(results)

string1 = 'a111bc123b'

# 需求：提取a字符和b字符之间的内容。
# .*：是贪婪匹配，在符合规则的前提下，尽可能多的匹配内容；
# .*?：是非贪婪匹配，在符合规则的前提下，尽可能少的匹配内容；
# p1 = re.compile(r'a(.*)b', re.S)
p1 = re.compile(r'a(.*?)b', re.S)
res = re.findall(p1, string1)
print(res)

# urllib进行GET请求
string2 = """

<h2>
极乐图腾
</h2>
</a>
<div class="articleGender manIcon">69</div>
</div>

<a href="/article/121378912" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>

在朋友圈看到一个人发的古装照，猜猜我是哪个年代的，猜对有奖，结果我回复了宋朝的，她回！确实有点像，我回！你觉得像就默认了，奖励什么呀，年轻人是要讲诚信的，不一会微信里收个红包。8.88,我不好意思的收下了，然后我说给你个机会赢回去，给你出个字迷，猜对也有奖，，他笑笑给我发了小孩上学的照片，我问你是老师吗，我说老师也没关系，不一定能猜出来，我给他发了！《一家四口养条狗，》（打一字）结果秒回，，还答对了，我就给他发了红包，我是不是有点不自量力了，那老师狂发捂嘴笑表情。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">404</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121378912" data-share="/article/121378912" id="c-121378912" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">9</i> 评论
</a>
"""
p2 = re.compile(r'<h2>(.*?)</h2>.*?<div.*?>(.*?)</div>.*?<span>(.*?)</span>', re.S)
res1 = re.findall(p2, string2)
print(res1)

from urllib.request import urlopen, Request
# 向一个地址发送GET请求
req = Request(url='https://www.qiushibaike.com/hot/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'})
response = urlopen(req)
# <class 'bytes'>获取的是字节码对象，需要转化成str对象
# print(type(response.read()))
# 字节码中文是编码之后的数据：\xe4\xbd\xbf\xe7\x94\xa8 \xe5\xbe\xae\xe4\xbf\xa1
# decode()：将<class 'bytes'>类型的数据转化成<class 'str'>
html_string = response.read().decode()
print(html_string)
# 接下来，你需要利用正则表达式，从html_string这个字符串中，提取数据。



