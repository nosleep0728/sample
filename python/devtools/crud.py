# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 27.

CRUD 문장을 만드는 프로그램.

@author: dulee
'''

import util

#c = """aa,bb,cc,dd"""
#c = 'DISEN_SN,BSNS_YEAR,CMPTNC_INSTT_CODE,CMPTNC_LWPRT_INSTT_CODE,CPR_NM,RPRSNTV_NM,FOND_DE,ZIP,LEGALDONG_CODE,ADRES_DETAIL,RN_ADRES,EMD_SN,RN_ADRES_DETAIL,USE_AT,REGISTER_ID,REGIST_DE,UPDUSR_ID,UPDT_DT'


def mk_insert(mydict, cols):
	s = ""
	s += "INSERT INTO table (\n"
	first = util.First()
	for col in cols:
		col = col.strip()
		if not first.isFirst():
			s += ",\n"
		s += '\t' + col 
	s += "\n)VALUES( \n"
	first = util.First()
	for col in cols:
		col = col.strip()
		if not first.isFirst():
			s += ", \n"
		s += "\t'0' /* {col} */".format(col=col)
	s += "\n)"
	return s

def mk_insert2(mydict, cols):
	s = ""
	s += "INSERT INTO table (\n"
	first = util.First()
	for col in cols:
		col = col.strip()
		if not first.isFirst():
			s += ", \n"
		s += '\t' + col
	s += "\n)VALUES( \n"

	for col in cols:
		col = col.strip()

		col2 = '#' + util.underscore_to_camel(col) + '#,'
		#col2 = col
		hanname = util.eng_to_han_one(mydict, col)
		s += "\t{col:25}/* {hanname} */\n".format(col=col2, hanname=hanname)
	s += "\n)"
	s = util.rm_last_one_char(s, ',')
	return s



def mk_update(mydict, cols):
	s = ""
	s += "UPDATE table SET\n"
	for col in cols:
		col = col.strip()
		col2 = '#' + util.underscore_to_camel(col) + '#,'
		#col2 = col
		hanname = util.eng_to_han_one(mydict, col)
		s += "\t{col:25} = {col2:25} /* {hanname} */\n".format(col=col,col2=col2, hanname=hanname)
	
	s += "\nWHERE 1=1"
	s = util.rm_last_one_char(s, ',')
	return s


def mk_select(mydict, cols):
	s = ""
	s += "SELECT \n"
	for col in cols:
		col = col.strip()
		hanname = util.eng_to_han_one(mydict, col)
		col += ','
		s += "\t{col:25} /* {hanname} */\n".format(col=col,hanname=hanname)
	s += "\nFROM table"
	s += "\nWHERE 1=1"
	s = util.rm_last_one_char(s, ',')
	return s

if __name__ == "__main__":
	c = 'DISEN_SN,BSNS_YEAR,IHIDNUM,BIZRNO,TLPHON_NO,MOBLPHON_NO,EMAIL,DELNG_BANK_CODE,ACNUT_NO,ACNUT_OWNER_NM,FXNUM,RPRSNTV_ID,RPRSNTV_TLPHON_NO,RPRSNTV_MOBLPHON_NO,FARMNG_MNGMTSYS_ID'
	c = 'BSNS_YEAR,AGBS_CODE,VILAGE_REQST_SN,CMPTINST_CODE,CMPTNC_LWPRT_INSTT_CODE,VILAGE_NM,RPRSN_TV_NM,RPRSN_TV_ADRES_CODE,RPRSN_TV_ADRES_DETAIL,RPRSN_TV_RN_ADRES_CODE,RPRSN_TV_EMD_SN,RPRSN_TV_RN_ADRES_DETAIL,REQST_DE,REQST_STTUS_CODE,CHARGER_OPINION,USE_AT,LEGALDONG_CODE,REGISTER_ID,REGIST_DT,UPDT_DT,UPDUSR_ID'
	cols = util.split(c)
	
	mydict = util.load_file("dict.txt")
	print ""
	print mk_insert(mydict, cols)
	print ""
	print mk_insert2(mydict, cols)
	print ""
	print mk_update(mydict, cols)
	print ""
	print mk_select(mydict, cols)
