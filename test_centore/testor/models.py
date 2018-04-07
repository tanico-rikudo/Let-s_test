# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import django

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.
class Member(models.Model):
	created_at  = models.DateTimeField('登録日',auto_now_add=True)
	updated_at  = models.DateTimeField('変更日',auto_now=True)
	name = models.CharField('Username', max_length=255)
	email = models.CharField('E-Mail', max_length=255)
	age = models.IntegerField('Age', blank=True, default=0)

	def __str__(self):
		return self.name


# Create your models here.
class Test(models.Model):
	created_at  = models.DateTimeField('登録日',auto_now_add=True)
	updated_at  = models.DateTimeField('変更日',auto_now=True)
	name = models.CharField('テスト', max_length=255)


	def __str__(self):
		return self.name

class Result(models.Model):
	created_at  = models.DateTimeField('登録日',auto_now_add=True)
	updated_at  = models.DateTimeField('変更日',auto_now=True)
	username    = models.ForeignKey(Member,verbose_name = 'ユーザ')
	testname    = models.ForeignKey(Test,verbose_name = 'テスト')

	# def __str__(self):
	# 	return self.name