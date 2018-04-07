# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from testor.models import Member,Test,Result
from django.contrib.auth.decorators import login_required

import middles as md

from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'index.html')

@login_required#ログインが必要な場合
def member_index(request):
	# return HttpResponse("Indexです！")
	# return HttpResponse("Indexです！")
	# return render(request, 'members/index.html')
	members = Member.objects.all().order_by('id') #値を取得
	return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す

@login_required#ログインが必要な場合
def test_index(request):
	tests = Test.objects.all().order_by('id') #値を取得
	user_id = request.user.id
	return render(request, 'tests/index.html', {'tests':tests,'user_id':user_id}) #Templateに値を渡す

@login_required#ログインが必要な場合
def result_index(request):
	results = Result.objects.all().order_by('id') #値を取得
	return render(request, 'results/index.html', {'results':results}) #Templateに値を渡す

@login_required#ログインが必要な場合
def middle_index(request):
	try:

		if str(request.POST['user_id']) == str(request.user.id): ##本人確認
			if request.POST['user_id'] and request.POST['q_no'] and request.POST['url'] and request.POST['test']:#途中経過
				if request.POST['q_no'] == 'start': #初回の場合#始まり確認
					middles = md.controll_test(request.POST)
					return  render(request, 'middle/index.html', {'middles':middles}) #Templateに値を渡す
				else:
					##保存処理と次を取得処理書く
					print 'rr'
					middles = md.controll_test(request.POST)
					print 'rr'
					if middles['q_no'] != 'end': #もし修了なら
						return  render(request, 'middle/index.html', {'middles':middles}) #Templateに値を渡す
					else:
						return  render(request, 'middle/finish.html') #Templateに値を渡す



	except Exception as e:
		return  e
