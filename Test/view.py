from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

def Login(request):
    if request.method == 'GET':
#创建参数字典
        result = {}
        username = request.GET.get('username')
        telnum = request.GET.get('telnum')
        date = request.GET.get('date')
        result['username'] = username
        result['telnum'] = telnum
        result['date'] = date
	#把字典转换成json
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
    #返回login页面
        return render_to_response('login.html')
