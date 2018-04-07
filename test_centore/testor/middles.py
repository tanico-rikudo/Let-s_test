# -*- coding: utf-8 -*-
import pandas as pd
import json,csv
from django.contrib.auth.models import User

folder = 'files/'
def controll_test(post):
	### 保存処理 ###
	print "d1"
	filename = folder+'result_'+str(post['user_id'])+'_'+str(post['test'])+'.json'
	if post['q_no'] == 'start':
		##　初めて　##
		print "d2"
		with open(filename,'w') as f:
			json.dump(post, f)
			f.write('\n')
		next_no = 0

	else:
		print "d3"
		with open(filename,'a') as f:
			json.dump(post, f)
			f.write('\n')
		print int(post['q_no'])
		next_no = int(post['q_no'])+1
		print next_no

	### 次回の情報 ###
	print "d4"
	resource_file = folder+'resource_'+post['test']+'.csv'

	with open(resource_file,'r') as f:
		middle = {}
		print "dd"
		readlines = csv.reader(f)
		print 'ddd'
		for i , line in enumerate(readlines):

			if i == next_no:
				middle['url'] = line[1]
				middle['q_no'] = line[0]
				middle['user_id'] = post['user_id']
				middle['test']= post['test']
				print line
				return middle

		middle['q_no'] = 'end'	
		return middle
