from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),

    # 上传文件路由
    url(r'^upfile/$', views.upfile),
    url(r'^savefile/$', views.savefile),

    # 学生列表信息分页
    url(r'^studentpage/(\d+)$', views.studentpage),

    # 显示学生信息
    url(r'^showstudents/$', views.showstudents),
    url(r'^studentsinfo/$', views.studentsinfo),
]