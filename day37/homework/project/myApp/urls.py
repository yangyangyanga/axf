from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^base/$', views.base),
    url(r'^baseindex/$', views.baseindex, name='baseindex'),
    url(r'^base1/$', views.base1),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^usercenter/$', views.usercenter, name='usercenter'),
    url(r'^shoppingcar/$', views.shoppingcar, name='shoppingcar'),
    url(r'^login/$', views.login, name='login'),
    url(r'^verifycode/$', views.verifycode, name='verifycode'),
    url(r'^verifycodefile/$', views.verifycodefile),
    url(r'^verifycodecheck/$', views.verifycodecheck),
]