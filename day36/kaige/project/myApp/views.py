from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')

def attributes(request):
    # /sunck/attributes/
    # GET
    # None
    # <QueryDict: {}>
    # <QueryDict: {}>
    # <MultiValueDict: {}>
    # {'csrftoken': '1neNROcLpnVAuU9naKMuz5oWZ7sHo2w5XyIYuCMlFy6uoc2KNk4ECG7aRsoeZtry'}
    # <django.contrib.sessions.backends.db.SessionStore object at 0x00000143623896D8>
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)

    return HttpResponse("attributes")

# 获取get传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)


def get2(request):
   a = request.GET.getlist('a')
   a1 = a[0]
   a2 = a[1]
   c = request.Get.get('c')
   return HttpResponse(a1 + " " + a2 + " " + c)

# POST
# 展示注册表单界面
def showregist(request):
    return render(request, 'myApp/regist.html')
def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)

    return HttpResponse("注册成功")

# response
def showresponse(request):
    # b''
    # utf - 8
    # 200
    res = HttpResponse()
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

#cookie
def cookietest(request):
    res = HttpResponse()
    # cookie =
    # res.write("<h1></h1>")
    cookie = res.set_cookie("sunck","good")
    return res

# 重定向
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect('/sunck/redirect2/')
    return redirect('/sunck/redirect2/')
def redirect2(request):
    # if request.is_ajax():
    #     a = JsonResponse({})

    return HttpResponse("我是重定向后的视图")


# session
def main(request):
    # 取session，没取到就是后面的值
    username = request.session.get('name', "游客")
    print(username)
    return render(request, 'myApp/main.html',{"username": username})
def login(request):
    return render(request, 'myApp/login.html')
def showmain(request):
    print("****")
    username = request.POST.get('username')
    # 存储session
    # 过期时间
    # request.session.set_expiry(10)
    request.session['name'] = username

    return redirect('/sunck/main/')
# 退出登录
from django.contrib.auth import logout
def quit(request):
    # 清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/sunck/main')



