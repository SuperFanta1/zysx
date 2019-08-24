from django.shortcuts import render
import requests, json

def index(request):
    """
    天气视图函数
    :param request:
    :return:
    """
    feture_data_dict = {}
    city = request.GET.get('city', '郑州市')
    url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city)
    json_str = requests.get(url).text
    weather_dict = json.loads(json_str)
    weather_data = weather_dict['results'][0]['weather_data']
    # 获取当前的天气信息
    current_data_dict = weather_data[0]
    # 获取未来三天的天气信息
    feture_data = [weather_data[1], weather_data[2], weather_data[3]]

    feture_data_dict['feture_data'] = feture_data
    feture_data_dict['current_data'] = current_data_dict
    feture_data_dict['city_name'] = city

    # feture_data_dict数据结构如下：
    # {
    #     'feture_data': [{}, {}, {}],
    #     'current_data': {},
    #     ...
    # }
    return render(request, template_name='weather.html', context=feture_data_dict)
