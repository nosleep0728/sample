# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 5.

@author: dulee
'''

import util



def get_columns(asize):
	i = 0
	s = "<Columns>\n"
	for data in asize:
		data = data.strip()
	
		s += """<Column size="{data}" />\n""".format(data=data)
		i += 1
	
	s += "</Columns>\n\n"
	return s

def get_columns_bylen(a):
	size = util.get_size_str(len(a))
	asize = size.split(",")
	return get_columns(asize)

def get_band_head(ahead):
	i = 0;
	s = """<Band id="head">\n"""
	for data in ahead:
		data = data.strip().replace(' ','&#32;')
		if i == 0 :
			s += """<Cell text="{data}"/>\n""".format(data=data)
		else:
			s += """<Cell col="{id}" text="{data}"/>\n""".format(id=i,data=data)
		i += 1
	
	s += "</Band>\n\n"
	return s

def get_band_body(abody):  
	i = 0;
	s = """<Band id="body">\n"""
	for data in abody:
		data = data.strip()
		if i == 0 :
			s += """<Cell text="bind:{data}"/>\n""".format(data=data)
		else:
			s += """<Cell col="{id}" text="bind:{data}"/>\n""".format(id=i,data=data)
		i += 1
	s += "</Band>\n"
	
	s += "\n"
	return s


if __name__ == '__main__':
	pass

	
	#head = "등급,생산량(kg)"
	head = "등급	자부담비율(%)	건초->사일리지 변환 가중치	톤당 지원금액"
	
	
	# 탭이 있으면, 탭으로 분리하도록 처리함. 
	ahead = util.split(head)
		
	
	body = util.get_col_str(len(ahead))
	
	
	abody = body.split(",")
	
	
	
	print get_columns_bylen(ahead)
	
	# head band 
	
	
	print get_band_head(ahead)
	
	# body band
	
	print get_band_body(abody)

