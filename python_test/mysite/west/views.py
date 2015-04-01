#!/usr/bin/env python
# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from models import Character
from django.core.context_processors import csrf
from django import forms

class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form'] = form
    return render(request, "investigate.html", ctx)
