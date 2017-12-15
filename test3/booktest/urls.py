from django.conf.urls import url
from booktest import views

urlpatterns = [
    # url('^(\d+)/(\d+)/$', views.index)
    url(r'^(?P<canshu1>\d+)/(?P<canshu2>\d+)/$', views.index),
    url(r'^get$', views.get),
    url(r'^wish$', views.wish),
    url(r'^post$', views.post),
    url(r'^post1/$', views.post1),  # 获取表单提交的参数
    url(r'^json$', views.json),
    url(r'^json1$', views.json1),
    url(r'^variable$', views.variable),
    url(r'^label$', views.label),
    url(r'^filter_test$', views.filter_test),
    url(r'^filter_test2$', views.filter_test2),
    url(r'^inherit$', views.inherit),
    url(r'^reverse_de/$', views.reverse_de),
    url(r'^reverse_de111/$', views.reverse_de1, name='reverse_de1'),
    url(r'^redirect$', views.redirect, name='reverse_red'),
    url(r'^redirect2$', views.redirect2, name='reverse_red'),
    url(r'^reverse3/(\d+)/(\d+)/$', views.reverse3, name='reverse3'),
    url(r'^transfer/$', views.transfer),
    url(r'^csrf/$', views.csrf),
    url(r'^csrf1/$', views.csrf1),

    url(r'^login$', views.login),
    url(r'^verify/$', views.verify),
    url(r'^login_check$', views.login_check),

    url(r'^staticfile$', views.staticfile),

    url(r'^pic_upload$', views.pic_upload),
    url(r'^pic_handle/$', views.pic_handle),
    url(r'^pic_show/$', views.pic_show),

    url(r'^page(\d*)/$', views.pagelist),

    url(r'^area/$', views.area_select),
    url(r'^areas/$', views.areas),
]

