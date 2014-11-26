# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 27.

@author: dulee
'''
# 파일의 내용중, 한글을 인식하게 하기 위해서는 # -*- coding: utf-8 -*- 가 필요함.
import cx_Oracle
import util


sql = '''
select a.* , b.* from 
TN_BUF_DISEN a , TN_BUF_DISEN_IVINF b 
where A.BSNS_YEAR = B.BSNS_YEAR and A.DISEN_SN = B.DISEN_SN  and 1 = 2
'''
#sql = '''select * from TN_BUF_DISEN_IVINF '''
sql = 'select * from AMES.TN_BUF_DISEN_IVINF'
#import os
#os.putenv("NLS_LANG", "KOREAN_KOREA.KO16KSC5601") 


con = cx_Oracle.connect("ID/암호@주소:1521/sid")

cursor = con.cursor()

cursor.execute(sql)

'''
while True:
	row = cursor.fetchone()
	if(row == None):
		break

	print row
	for col in row:
		#print "type" + str(type(col))
		if type(col) != str:
			#print "pass........................."
			continue
		# 한글을 제대로 출력하기 위함. 
		print unicode(col, "cp949")	
'''



cols = cursor.description

def get_type_str(t):
	s = "String"
	if( t == cx_Oracle.STRING ):
		s = "String"
	elif(t == cx_Oracle.NUMBER):
		s = "Long"
	return s

for col in cols:
	#print col
	(name, t) = col[0],col[1]
	print get_type_str(t) + " " +util.underscore_to_camel(name) + " ;" 


s= ""
first = util.First()
for col in cols:
	(name, t) = col[0],col[1]
	if not first.isFirst():
		s += ","
	s += name
	
print ""
print s

sl = s.lower()
print ""
print sl
print ""
print util.underscore_to_camel(sl)

