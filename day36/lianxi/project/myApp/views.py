from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')

# HttpRequest属性
def attributes(request):
    # / yang / attributes /
    # GET
    # None
    # < QueryDict: {} >
    # < QueryDict: {} >
    # < MultiValueDict: {} >
    # {'csrftoken': '1neNROcLpnVAuU9naKMuz5oWZ7sHo2w5XyIYuCMlFy6uoc2KNk4ECG7aRsoeZtry', 'sessionid': 'ensclx132q3edy2jb3pgn627wyz5lgu8'}
    # < django.contrib.sessions.backends.db.SessionStore object at 0x0000022F17B29B70 >
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("测试HttpRequest属性----")

#  HttpRequest中的GET属性
def get1(request):
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)
def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + " " + a2 + " " + c)

# HttpRequest中的POST属性
def showregist(request):
    return render(request, 'myApp/regist.html')
def regist(request):
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    hobby = request.POST.get('hobby')
    print(name)
    print(sex)
    print(hobby)
    return HttpResponse("注册成功" + " " + name + " " + sex + " " + hobby)

#  HttpResponse属性
def showresponse(request):
    res = HttpResponse()
    print("content = ", res.content)
    print("charset = ", res.charset)
    print("status_code = ", res.status_code)
    # print("content-type = ", res.content-type)
    return res

#  HttpResponse方法
def cookietest(request):
    res = HttpResponse()
    # cookie = request.COOKIES
    # res.write("<h1>" + cookie['sunck'] + "</h1>")
    cookie = res.set_cookie('yang1', "good")
    return res

# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect('/yang/redirect2/')
    return redirect('/yang/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向后的视图。。。")

# 状态保持 == 使用session
def main(request):
    # 取session
    username = request.session.get('name', '游客')

    return render(request, 'myApp/main.html', {"username": username})
def login(request):
    return render(request, 'myApp/login.html')
def showmain(request):
    # request.session.set_expiry(5)
    username = request.POST.get('username')
    request.session['name'] = username
    return redirect('/yang/main')
from django.contrib.auth import logout
def quit(request):
    # 清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/yang/main')





