# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Indexです！")
    # return HttpResponse("Indexです！")
    # return render(request, 'members/index.html')
    members = Member.objects.all().order_by('id') #値を取得
    return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す