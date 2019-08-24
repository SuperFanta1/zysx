from django.shortcuts import render
import requests, json


def index(request):
    context = {}
    city = request.GET.get('city', '郑州市')
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
    json_str = requests.get(url).text
    json_dict = json.loads(json_str)
    error = json_dict['error']
    status = json_dict['status']
    if error == 0 and status == 'Success':
        # 请求成功
        movies = json_dict['result']['movie']
        if len(movies) == 0:
            context['errormsg'] = '暂时没有电影信息'
        else:
            context['movies'] = movies
    else:
        # 请求失败
        context['errormsg'] = '请求接口失败'

    return render(request, template_name='movie.html', context=context)
