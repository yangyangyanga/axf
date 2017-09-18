from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man")
    # return render(request,'myApp/index.html')
    # return HttpResponse("<h1>sunck is a good man</h1>")
# 父模板
def base(request):
    return render(request, 'myApp/base.html')
def base1(request):
    return render(request, 'myApp/base1.html')
def baseindex(request):
    return render(request, 'myApp/baseindex.html')
def detail(request):
    return render(request, 'myApp/detail.html')
def usercenter(request):
    return render(request, 'myApp/usercenter.html')
def shoppingcar(request):
    return render(request, 'myApp/shoppingcar.html')
def login(request):
    return render(request, 'myApp/login.html')

def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\AdobeArabic-Bold.otf', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verify'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'img/png')

def verifycodefile(request):
    f = request.session.get('flag', True)
    str = ""
    if f == False:
        str = "请重新输入"
    request.session.clear()
    return render(request, 'myApp/verifycodefile.html',{'flag': str})
from django.shortcuts import redirect
def verifycodecheck(request):
    code1 = request.POST.get('verifycode').upper()
    code2 = request.session['verify'].upper()
    if code1 == code2:
        return render(request, 'myApp/success.html')
    else:
        request.session['flag'] = False
        return redirect('/sunck/verifycodefile')

