from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myApp/welcome.html')

from .models import Students,Grades
def students(request):
    studentList = Students.stuObj1.all()
    return render(request, "myApp/students.html", {"students": studentList})

def addstudent(request):
    # 获得grades的一个对象
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent('lalala', True, 35, "我叫啦啦啦", grade)
    stu.save()
    return HttpResponse("添加成功")

def addstudent1(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj1.createstudent('lalala1', True, 35, "我叫啦啦啦", grade)
    stu.save()
    return HttpResponse("添加成功1")

def students1(request):
    # 报异常
    studentsList = Students.stuObj1.get(ssex=True)
    return HttpResponse("报异常")

# 显示前五条学生
def students2(request):
    studentsList = Students.stuObj1.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})

# 分页显示学生
def stupage(request, page):
    page = int(page)
    studentsList = Students.stuObj1.all()[(page-1) * 5: page * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})

from django.db.models import Max
def studentsearch(request):
    # studentsList = Students.stuObj1.filter(sname__contains = '啦')
    # studentsList = Students.stuObj1.filter(sname__startswith='l')
    # studentsList = Students.stuObj1.filter(sage__gt=20)
    studentsList = Students.stuObj1.filter(pk__in=[2, 4, 6, 8, 10])
    # 描述中带有'薛延美'这三个字的数据时属于哪个班级的
    grade = Grades.objects.filter(students__scontend__contains="薛延美")
    print(grade)

    maxAge = Students.stuObj1.aggregate(Max('sage'))
    print(maxAge)
    return render(request, 'myApp/students.html', {"students": studentsList})

from django.db.models import F,Q
def grades(request):
    g = Grades.objects.filter(ggirlnum__lt=F('gboynum')+20)
    print(g)
    return HttpResponse("------------")