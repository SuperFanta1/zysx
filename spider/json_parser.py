# 爬虫中也经常会遇到以JSON数据返回内容的网站，这种网站不再需要使用正则表达式匹配文本，直接分析网站是否含有接口返回JSON，如果有，直接使用json.loads()对json字符串进行解析就可以获取数据。

# pip install requests：比较流行的第三方请求库，用法更加简单。

import requests

response = requests.get('https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=721&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.57864850&x-zp-page-request-id=300f5817f60c495e9c8c067e2b23e14b-1547017763916-820057')
print(response)
# 响应状态码：GET请求成功的响应码是200；POST：成功状态码是201；
# 401、400、403、404等以4开头的状态码表示程序代码有问题；
# 500、501、501、505等以5开头的状态码表示你所访问的网站服务器有问题，跟代码关系不大；

json_str = response.text
# json字符串：是有自己的语法格式；
"""
{   
    "code": 200,
    "data": [
        {"a": 1},
        {"a": 1},
        {"a": 1}
    ]
}
"""

import json

# json_dict是最外层的字典，内部有两个键值对
# code: 200和data: {numFound: 35, numTotal: 35,…}
json_dict = json.loads(json_str)

# data: {numFound: 35, numTotal: 35,…}
data_dict = json_dict['data']

results = data_dict['results']

for item_dict in results:
    city = item_dict['city']['display']
    company = item_dict['company']['name']
    edu = item_dict['eduLevel']['name']
    job_name = item_dict['jobName']
    job_type = item_dict['jobType']['display']
    # ';'.join()：使用;字符将列表中的每一个元素拼接起来，得到一个字符串；
    welfare = ';'.join(item_dict['welfare'])
    workingExp = item_dict['workingExp']['name']

    print('城市：{}; 公司名称：{}; 学历要求：{}; 招聘职位：{}; 职位类型：{}; 福利待遇：{}; 工作经验：{}'.format(city, company, edu, job_name, job_type, welfare, workingExp))
