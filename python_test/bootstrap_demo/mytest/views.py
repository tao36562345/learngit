#coding:utf-8
from django.shortcuts import render, render_to_response

# Create your views here.
def demo01(req):
    return render_to_response('demo01.html')
