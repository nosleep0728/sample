'''
Created on 2014. 9. 16.

@author: dulee
'''
import util

class BindItemVar:
	
	def columnidToArr(self, arr):
		arrRow = []
		for item in arr:
			assert isinstance(item, str)
			idx = item.find('columnid="')
			if( idx < 0 ): continue
			item = item[idx + 10:]
			idx = item.find('"')
			if( idx < 0): continue
			item = item[:idx]
			camel = util.underscore_to_camel(item.lower())
			arrRow.append({'item':item,'camel':camel})
		return arrRow

	def bindToArr(self, arr):
		arrRow = []
		for item in arr:
			assert isinstance(item, str)
			idx = item.find('"bind:')
			if( idx < 0 ): continue
			item = item[idx + 6:]
			idx = item.find('"')
			if( idx < 0): continue
			item = item[:idx]
			camel = util.underscore_to_camel(item.lower())
			arrRow.append({'item':item,'camel':camel})
		return arrRow
	
	def __init__(self,s, mydict):
		self.mydict = mydict
		arr = s.splitlines()

		arrRow = self.columnidToArr(arr);
		if(len(arrRow) == 0 ):
			arrRow = self.bindToArr(arr)
		self.arrRow = arrRow
	
	def getVarStr(self):
		s = 'var irow = 0,\n'
		arrRow = self.arrRow
		for row in arrRow:
			line = "\t%-25s = ds.getColumn(irow,'%s'),\n" % ( row['camel'] , row['item'])
			s += line
		s = util.rm_last_one_char(s,',')
		s += '\t;'
		return s
	
	def getChkStr(self):
		s = ''
		arrRow = self.arrRow
		s += 'var arr = ['
		first = util.First()
		for row in arrRow:
			if( not first.isFirst()):
				s += ','
			line = "\n\t{chk:false, val:%-25s,msg:'' }" % ( row['camel'] )
			s += line
		s += '\n\t];\n'
		s += 'return buf.isValidParam(arr);\n'
		return s
	
	def getChkStr2(self):
		s = ''
		arrRow = self.arrRow
		s += 'row = buf.dsRowToObj({ds:ds,irow:0});\n'
		s += 'var arr = ['
		first = util.First()
		for row in arrRow:
			if( not first.isFirst()):
				s += ','
			hanname = util.eng_to_han_one(self.mydict, row['item'])
			line = "\n\t{chk:false, val:row.%-25s,msg:'%s' }" % ( row['item'], hanname )
			s += line
		s += '\n\t];\n'
		s += 'return buf.isValidParam(arr);\n'
		return s
	
	def getChkStr3(self):
		s = ''
		arrRow = self.arrRow
		s += 'row = buf.dsRowToObj({ds:ds,irow:0});\n'
		s += 'var arr = ['
		first = util.First()
		for row in arrRow:
			if( not first.isFirst()):
				s += ','
			hanname = util.eng_to_han_one(self.mydict, row['item'])
			colname = "'" + row['item'] + "'"
			line = "\n\t{chk:true , col:%-25s,msg:'%s' }" % ( colname, hanname )
			s += line
		s += '\n\t];\n'
		s += 'return buf.isValidRow(row,arr);\n'
		return s
			

if __name__ == '__main__':
	pass

	s1 = '''
	<Bind>
	  <BindItem id="item0" compid="cbo_year" propid="value" datasetid="ds_detail" columnid="BSNS_YEAR"/>
	  <BindItem id="item1" compid="cbo_wk" propid="value" datasetid="ds_detail" columnid="CMPTNC_INSTT_CODE"/>
	  <BindItem id="item2" compid="cbo_em" propid="value" datasetid="ds_detail" columnid="CMPTNC_LWPRT_INSTT_CODE"/>
	  <BindItem id="item3" compid="Edit00" propid="value" datasetid="ds_detail" columnid="CPR_NM"/>
	  <BindItem id="item4" compid="Edit01" propid="value" datasetid="ds_detail" columnid="BIZRNO"/>
	  <BindItem id="item5" compid="Edit02" propid="value" datasetid="ds_detail" columnid="RPRSNTV_NM"/>
	  <BindItem id="item6" compid="Edit11" propid="value" datasetid="ds_detail" columnid="FARMNG_MNGMTSYS_ID"/>
	  <BindItem id="item7" compid="Edit09" propid="value" datasetid="ds_detail" columnid="ADRES_DETAIL"/>
	  <BindItem id="item8" compid="Edit10" propid="value" datasetid="ds_detail" columnid="RN_ADRES_DETAIL"/>
	  <BindItem id="item9" compid="Edit04" propid="value" datasetid="ds_detail" columnid="RN_ADRES"/>
	  <BindItem id="item10" compid="Edit05" propid="value" datasetid="ds_detail" columnid="EMAIL"/>
	  <BindItem id="item11" compid="Edit08" propid="value" datasetid="ds_detail" columnid="FXNUM"/>
	  <BindItem id="item12" compid="edt_acnutNo" propid="value" datasetid="ds_detail" columnid="ACNUT_NO"/>
	  <BindItem id="item13" compid="edt_acnutOwnerNm" propid="value" datasetid="ds_detail" columnid="ACNUT_OWNER_NM"/>
	  <BindItem id="item14" compid="cbo_bank" propid="value" datasetid="ds_detail" columnid="DELNG_BANK_CODE"/>
	  <BindItem id="item15" compid="Edit06" propid="value" datasetid="ds_detail" columnid="TLPHON_NO"/>
	  <BindItem id="item16" compid="Edit07" propid="value" datasetid="ds_detail" columnid="MOBLPHON_NO"/>
	  <BindItem id="item17" compid="Edit03" propid="value" datasetid="ds_detail" columnid="ADRES"/>
	</Bind>
'''
	s = '''
				<Cell col="1" text="bind:BUF_GRAD_CODE_NM" editlimit="-1"/>
				<Cell col="2" displaytype="number" edittype="masknumber" text="bind:MCT_POCTPAYM__RATE" mask="99%" editlimit="2" editlimitbymask="both"/>
				<Cell col="3" displaytype="number" edittype="masknumber" text="bind:MCT_DRYGRASS_SILAGE_WGHTVAL" mask="9.9" editlimit="3" editlimitbymask="both" suppress="0"/>
				<Cell col="4" displaytype="number" edittype="masknumber" text="bind:MCT_SPORT_TON_AMOUNT" mask="99,999" editlimit="5" editlimitbymask="both" combodisplayrowcount="5"/>
			  </Band>
'''

	print ''
	mydict = util.load_file("dict.txt")
	o = BindItemVar(s, mydict)
	print o.getVarStr();
	print ''
	print ''
	print o.getChkStr()
	print ''
	print o.getChkStr2()
	print ''
	print o.getChkStr3()


		