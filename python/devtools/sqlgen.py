# -*- coding: utf-8 -*-
'''
Created on 2014. 10. 15.

@author: dulee
'''



farm = '''
	<sql id="c2020101.cmmn.eqjoin.frlnd{a}{b}">
		AND {a}.BSNS_YEAR = {b}.BSNS_YEAR AND {a}.AGBS_CODE = {b}.AGBS_CODE AND {a}.REQST_SN = {b}.REQST_SN AND {a}.REQST_FRLND_SN = {b}.REQST_FRLND_SN 
	</sql>'''


reqst = '''
	<sql id="c2020101.cmmn.eqjoin.reqst{a}{b}">
		AND {a}.BSNS_YEAR = {b}.BSNS_YEAR AND {a}.AGBS_CODE = {b}.AGBS_CODE AND {a}.REQST_SN = {b}.REQST_SN 
	</sql>'''


#t = 'A,B,C,D,E'
t = 'AA,AB,BA,BB,CA,CB,DA,DB,EA,EB'


def getsqllist(ca, s):
	a = ca.split(',')
	msg = ''
	for aa in a:
		start = False
		for bb in a:
			if aa == bb :
				start = True
				continue
			if not start :
				continue
			msg += s.format(a=aa,b=bb)
	return msg

def getmultilist(colona,s):
	a = colona.split(':')
	msg = ''
	for i in a:
		msg += getsqllist(i,s)
	return msg


print '	<!-- 신청 -->'
print getsqllist('A,B,C,D,E',reqst)
print getsqllist('SA,SB,SC,SD,SE',reqst)
print getsqllist('AA,BA,CA,DA,EA',reqst)
print getmultilist('AA,AB:BA,BB:CA,CB:DA,DB:EA,EB',reqst)

print '	<!-- 신청농지 -->'
print getsqllist('A,B,C,D,E',farm)
print getsqllist('SA,SB,SC,SD,SE',farm)
print getsqllist('AA,BA,CA,DA,EA',farm)
print getmultilist('AA,AB:BA,BB:CA,CB:DA,DB:EA,EB',farm)








