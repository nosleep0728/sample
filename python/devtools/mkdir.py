# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 28.
디렉토리 생성 모듈.
@author: dulee
'''


import util
import os

ds = """

"""
ads = ds.split('\n')

for p in ads:
	if(p == "") :
		continue
	p = "." + p
	if( os.path.isdir(p)):
		continue
	print p
	os.makedirs(p)
	#os.makedirs(p + "/web")
	#os.makedirs(p + "/service/impl")
	





