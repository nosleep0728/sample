# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 28.

@author: dulee
'''
import cx_Oracle

def get_comment_info(constr,tablename):
	''' 코멘트 와 컬럼명을 이용한 코멘트리스트를 만드는 함수.
	    constr : 연결문자열
	    mydict : 용어사전. 코멘트가 없을 경우 사용.
	    cols   : 컬럼정보. 
	'''
	tablename = tablename.strip()
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


def get_sql_list(ca, s):
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



def get_sql_equal_join(ca):
	reqst = '''
<include refid="c2020101.cmmn.eqjoin.reqst{a}{b}"/>
AND {a}.BSNS_YEAR = {b}.BSNS_YEAR AND {a}.AGBS_CODE = {b}.AGBS_CODE AND {a}.REQST_SN = {b}.REQST_SN '''
	farm = '''
<include refid="c2020101.cmmn.eqjoin.frlnd{a}{b}"/>
AND {a}.BSNS_YEAR = {b}.BSNS_YEAR AND {a}.AGBS_CODE = {b}.AGBS_CODE AND {a}.REQST_SN = {b}.REQST_SN AND {a}.REQST_FRLND_SN = {b}.REQST_FRLND_SN '''
	s = ''
	s += get_sql_list(ca, farm)
	s += get_sql_list(ca, reqst)
	return s

def get_sql_out_plus_join(ca):
	reqst = '''
<include refid="c2020101.cmmn.eqjoin.reqst{a}{b}"/>
AND {a}.BSNS_YEAR = {b}.BSNS_YEAR(+) AND {a}.AGBS_CODE = {b}.AGBS_CODE(+) AND {a}.REQST_SN = {b}.REQST_SN(+) '''
	farm = '''
<include refid="c2020101.cmmn.eqjoin.frlnd{a}{b}"/>
AND {a}.BSNS_YEAR = {b}.BSNS_YEAR(+) AND {a}.AGBS_CODE = {b}.AGBS_CODE(+) AND {a}.REQST_SN = {b}.REQST_SN(+) AND {a}.REQST_FRLND_SN = {b}.REQST_FRLND_SN(+) '''
	s = ''
	s += get_sql_list(ca, farm)
	s += get_sql_list(ca, reqst)
	return s

def get_sql_plus_out_join(ca):
	farm = '''
<include refid="c2020101.cmmn.eqjoin.frlnd{a}{b}"/>
AND {a}.BSNS_YEAR(+) = {b}.BSNS_YEAR AND {a}.AGBS_CODE(+) = {b}.AGBS_CODE AND {a}.REQST_SN(+) = {b}.REQST_SN AND {a}.REQST_FRLND_SN(+) = {b}.REQST_FRLND_SN '''
	reqst = '''
<include refid="c2020101.cmmn.eqjoin.reqst{a}{b}"/>
AND {a}.BSNS_YEAR(+) = {b}.BSNS_YEAR AND {a}.AGBS_CODE(+) = {b}.AGBS_CODE AND {a}.REQST_SN(+) = {b}.REQST_SN '''
	s = ''
	s += get_sql_list(ca, farm)
	s += get_sql_list(ca, reqst)
	return s

