# -*- coding: utf-8 -*-
'''
Created on 2014. 9. 25.

@author: dulee
'''
import re
import util

def trans_one_var(s):
	a = s.splitlines()
	first = util.First()
	for s in a:
		if(s.strip() == ''):
			continue
		if( not first.isFirst() ):
			s = re.sub(r'(\s*)var( )',r'\1   \2',s)
		#s = re.sub(r'(\s+)=(\s+)', r'\1:\2',s)
		s = re.sub(r';',r',',s)
		print s

def trans_colon_to_equal(s):
	a = s.splitlines()
	for s in a:
		if(s.strip() == ''):
			continue
		s = re.sub(r'(\s+):(\s+)', r'\1=\2',s)
		print s


def reorder_colno(s):
	a = s.splitlines()
	col = 0
	for s in a:
		if(s.strip() == ''):
			continue
		
		s = re.sub(r'(col=)"\d+"', r'\1"' + str(col) + r'"',s)
		col +=1
		print s


s = '''




	<Cell text="bind:CHK_BOX_STTUS"/>
	<Cell col="1" text="bind:CMPTNC_LWPRT_INSTT_CODE_NM"/>
	<Cell col="2" text="bind:APPLCNT_NM"/>
	<Cell col="5" text="bind:REQST_SEASON_NM"/>
	<Cell col="331" text="bind:CNTRCT_AR"/>
	<Cell col="5" text="bind:PRDCTN_QY"/>
	<Cell col="6" text="bind:PYMNT_TRGET_AMOUNT"/>
	<Cell col="7" text="bind:SLCTN_STTUS_CODE_NM"/>
	<Cell col="38" displaytype="image" style="cursor:hand;" text="img::btn_grid_delete_N.png"/>


	
'''
		
#trans_one_var(s)
reorder_colno(s)

#trans_colon_to_equal(s)

	
	