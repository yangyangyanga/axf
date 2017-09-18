from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("sunck is a good man")

def detail(request, num, num1):
    return HttpResponse("detail-%s-%s"%(num, num1))

from .models import Grades,Students
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传给模板，模板在渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {"grades": gradesList})

def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students": studentsList})

def gradeStudents(request, num):
    # 获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    # 获得班级下的所有学生列表
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})











