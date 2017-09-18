from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^addstudent/$', views.addstudent),
    url(r'^addstudent2/$', views.addstudent2),

    url(r'^students3/$', views.students3),
    url(r'^stupage/(\d+)$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),
    url(r'^grades/$', views.grades),
]