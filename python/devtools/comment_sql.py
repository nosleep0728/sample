# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 27.

@author: dulee
'''
# 파일의 내용중, 한글을 인식하게 하기 위해서는 # -*- coding: utf-8 -*- 가 필요함.
import cx_Oracle
import util


sql = '''
select * from TN_BUF_DISEN a 
'''


def get_cols(constr, sql):
	con = cx_Oracle.connect("id/pass@host:1521/sid")
	
	
	cursor = con.cursor()
	
	cursor.execute(sql)
	cols = cursor.description
	cursor.close()
	return cols

def get_comment_info(constr,tablename):
	''' 코멘트 와 컬럼명을 이용한 코멘트리스트를 만드는 함수.
	    constr : 연결문자열
	    mydict : 용어사전. 코멘트가 없을 경우 사용.
	    cols   : 컬럼정보. 
	'''
	sql = '''
		SELECT COLUMN_NAME, COMMENTS FROM ALL_COL_COMMENTS WHERE TABLE_NAME = '{table}'
	'''.format(table=tablename)
	con = cx_Oracle.connect(constr)
	
	cursor = con.cursor()
	
	cursor.execute(sql)
	a = cursor.fetchall()
	cursor.close()
	dic = {}
	cols = []
	m = {'dic':dic,'cols':cols}
	for i in a:
		cols.append(i[0])
		if i[1] == None :
			continue
		dic[i[0]] = unicode(i[1],'cp949').replace('_',' ').encode('utf-8')
		
	return m
	
		
m = get_comment_info("id/pass@host:1521/sid", 'TN_AGBS_PROGRS')

import crud2

s = crud2.mk_insert2({}, m['dic'], m['cols'])
print s

'''
ks = m['dic'].keys()
for k in ks:
	print m['dic'][k]
print m['cols']
'''


