from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views

app_name = 'intern'

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^(?P<courses_Course>.+?)/(?P<batch_Batch_No>[0-9]+)/$', views.detail, name='detail'),


    url(r'^(?P<person_id>[0-9]+)/$', views.pdetail, name='pdetail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^internship/apply/(?P<pk>[0-9]+)/$', views.apply.as_view(), name='apply'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^base/', views.base, name='base'),
    url(r'^home/', views.home, name='home'),
    url(r'^career/', views.career, name='career'),
    url(r'^imggallery/', views.imggallery, name='imggallery'),
    url(r'^(?P<courses_Course>.+?)/$', views.cgallery, name='course_g'),



    ]