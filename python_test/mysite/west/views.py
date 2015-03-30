# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from models import Character
from django.core.context_processors import csrf

def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")

def templay(request):
    staffs = Character.objects.all()
    context = {'staffs': staffs}
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)

def investigate2(request):
    if request.POST:
        submitted = request.POST['staff']
        new_record = Character(name=submitted)
        new_record.save()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    return render(request, "investigate.html", ctx)