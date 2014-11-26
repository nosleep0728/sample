# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 5.

@author: dulee
'''
import util

def get_cell_bind(cols):
	i = 0
	s = ""
	for data in cols: 
		if i == 0 :
			s += """<Cell text="bind:'{data}'"/>\n""".format(data=data);
		else:
			s += """<Cell col="{id}" text="bind:'{data}"/>\n""".format(id=i,data=data)
		i += 1
	s += "\n\n"
	return s

def get_column_info(cols):
	s = "<ColumnInfo>\n"
	for data in cols:
		data = data.strip()
		s += """  <Column id="{data}" type="STRING" size="256"/>\n""".format(data=data)
	s +="</ColumnInfo>\n\n"
	return s


def get_rows(cols,rows):
	s = "<Rows>\n"
	s += "  <Row>\n"
	i = 0
	for row in rows :
		row = row.strip()
		s += """	<Col id="{id}">{data}</Col>\n""".format(id=cols[i],data=row)
		i += 1
	
	s += "  </Row>\n"
	s += "</Rows>\n\n"
	return s

if __name__ == '__main__':
	pass

	
	#s ="col1,col2,col3,col4,col5,col6,col7"
	#r = """안양농원; 정읍시 고부면 고부리 1234;1,000; 혼파;100;홍길동;정읍시 고부면 고부리"""
	
	
	#s ="col1,col2,col3,col4,col5,col6,col7,col8,col9"
	cols = 12
	r = """A등급 100"""
	
	rows = util.split(r)
	
	#s = util.get_col_str(len(rows))
	
	s= 'DISEN_SN,BSNS_YEAR,IHIDNUM,BIZRNO,TLPHON_NO,MOBLPHON_NO,EMAIL,DELNG_BANK_CODE,ACNUT_NO,ACNUT_OWNER_NM,FXNUM,RPRSNTV_ID,RPRSNTV_TLPHON_NO,RPRSNTV_MOBLPHON_NO,FARMNG_MNGMTSYS_ID'
	
	cols = s.split(',')
	
	print "BINDING INFO...\n\n";
	
	
	
	
	
	print get_cell_bind(cols)
	
	
	################################################################################
	# xml dataset.
	################################################################################
	
	
	print get_column_info(cols)
	
	
	print get_rows(cols,rows)
	
	print "\n\n"
	
	################################################################################
	# csv print.
	################################################################################
	def getcolstr():
		ret = ""
		first = util.First()
		for data in cols:
			data = data.strip()
			if( not first.isFirst() ):
				ret  += ","
			ret += data + ":STRING(256)"
		return ret
	
	def getdatastr():
		first = util.First()
		ret = ""
		for data in rows:
			data = data.strip()
			if not first.isFirst():
				ret += ","
			ret += '"' + data + '"'
		return ret
	
	# csv print.
	print "CSV:utf-8"
	print "Dataset:"
	print getcolstr()
	print getdatastr()
	
	
	# csv var print. 
	print ""
	print "var str = '';"
	print "str +='CSV:utf-8\\n';"
	print "str +='Dataset:\\n';"
	print "str +='" + getcolstr() + "\\n';"
	print "str +='" + getdatastr() + "\\n';"
	


