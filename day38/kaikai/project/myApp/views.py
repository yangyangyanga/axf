from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')

def upfile(request):
    return render(request,'myApp/upfile.html')

import os
from django.conf import settings
def savefile(request):
    if request.method == "POST":
        f = request.FILES['file']
        # 合成文件在服务器端的路径
        filePath = os.path.join(settings.MDEIA_ROOT,f.name)
        with open(filePath, "wb") as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")

from .models import Students
from django.core.paginator import Paginator
def studentpage(request, pageid):
    # 所有学生列表
    allList = Students.objects.all()
    paginator = Paginator(allList, 6)
    # 获得一个Page对象，页码pageid
    page = paginator.page(pageid)
    return render(request,'myApp/studentpage.html',
                  {'students': page})

# 显示学生信息页面视图
def ajaxstudents(requent):
    return render(requent, 'myApp/ajaxstudents.html')
from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname, stu.sage])
    return JsonResponse({"data":list})

# 自定义视图中使用富文本
def edit(request):
    return render(request,'myApp/edit.html')
# 保存自定义的视图
def saveedit(request):
    textareavalue = request.POST.get('str')

    return HttpResponse(textareavalue)

from .task import sunck
def celery(request):
    sunck.delay()#添加到celery中执行，不会阻塞
    return render(request,'myApp/celery.html')
