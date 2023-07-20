from django.http import  HttpResponse
from django.http import HttpResponseRedirect
import os
import json

POST_FORM = '''
<form method='post' action='post_test'>
    用户名:<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>
'''

def page_2003_view(request):
    strr = os.popen('date')
    res = strr.read()
    strr.close()
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(str(res)+html)

def print_view(request, num1, op, num2):
    if op == 'add':
        return HttpResponse(str(num1+num2))
    elif op == 'sub':
        return HttpResponse(str(float(num1/num2)))
    elif op == 'mul':
        return HttpResponse(str(num1*num2))
    else:
        return HttpResponse('op error')

def birthday_view(request, year, month, day):
    return HttpResponse('生日为%s年%s月%s日'  %(year,month,day))

def test_request(request):
    #print(request.GET)
    data = {'name': 'shaw',
    'age': 25,
    'height': '185cm'
    }

    return HttpResponse(json.dumps(data),content_type='application/json',status=200)
    #return HttpResponseRedirect('/page/2003')


def post_test(request):
    if request.method=='GET':
        return HttpResponse(POST_FORM)
    elif request.method=='POST':
        print('username is', request.POST['username'])
    return HttpResponse('post ok')