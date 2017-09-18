from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')

# 上传文件视图
def upfile(request):
    filePath = os.path.join(settings.MDEIA_ROOT, 'moon.jpg')
    return render(request, 'myApp/upfile.html', {"filepath": filePath})
import os
from django.conf import settings
def savefile(request):
    filePath = os.path.join(settings.MDEIA_ROOT, 'moon.jpg')
    if request.method == "POST":
        f = request.FILES['file']
        filePath = os.path.join(settings.MDEIA_ROOT, f.name)
        with open(filePath, "wb") as fb:
            for info in f.chunks():
                fb.write(info)
        return render(request, 'myApp/upfile.html', {"filepath":filePath})
    else:
        return render(request,'myApp/upfile.html', {"filepath": filePath})

from django.core.paginator import Paginator
from .models import Students
# 学生列表信息分页
def studentpage(request, pageid):
    # 获取全部学生对象
    stusall = Students.objects.all()
    # 获取一个Paginator对象
    stuslist1 = Paginator(stusall, 6)
    # 返回一个Page对象
    page = stuslist1.page(pageid)
    return render(request, 'myApp/studentpage.html', {"students": page})


# 显示学生信息
def showstudents(request):
    return render(request, 'myApp/showstudents.html')
from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    print(stus)
    list = []
    for info in stus:
        list.append([info.sname, info.sage])
    return JsonResponse({"indd": list})











