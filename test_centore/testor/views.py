# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from testor.models import Member,Test,Result

# Create your views here.
def index(request):
	return render(request, 'index.html')

# @login_required#ログインが必要な場合
def member_index(request):
	# return HttpResponse("Indexです！")
	# return HttpResponse("Indexです！")
	# return render(request, 'members/index.html')
	members = Member.objects.all().order_by('id') #値を取得
	return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す

# @login_required#ログインが必要な場合
def test_index(request):
	# return HttpResponse("Indexです！")
	# return HttpResponse("Indexです！")
	# return render(request, 'members/index.html')
	tests = Test.objects.all().order_by('id') #値を取得
	return render(request, 'tests/index.html', {'tests':tests}) #Templateに値を渡す

# @login_required#ログインが必要な場合
def result_index(request):
	# return HttpResponse("Indexです！")
	# return HttpResponse("Indexです！")
	# return render(request, 'members/index.html')
	results = Result.objects.all().order_by('id') #値を取得
	return render(request, 'results/index.html', {'results':results}) #Templateに値を渡す