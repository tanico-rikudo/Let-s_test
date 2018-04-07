# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testor.models import Member
from testor.models import Test
from testor.models import Result

# Register your models here.
admin.site.register(Member)
admin.site.register(Test)
admin.site.register(Result)