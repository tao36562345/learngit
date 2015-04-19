#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^demo01/', 'mytest.views.demo01', name='demo01'),
)
