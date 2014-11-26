# -*- coding: utf-8 -*-
'''
Created on 2014. 9. 12.

@author: dulee
'''
import traceback
import re
import pygtk
pygtk.require("2.0")
import gtk

import cx_Oracle
import util
import utildb
import crud
import crud2
import dataset
import grid
import myhelp
import bindItemToVar
import pango

class DbCols:
	con_str = ''
	def __init__(self):
		pass
	
	def get_type_str(self,t,precision, scale):
		s = "String"
		if( t == cx_Oracle.STRING ):
			s = "String"
		elif(t == cx_Oracle.NUMBER):
			if( scale > 0 ):
				s = "Float"
			else:
				if precision > 9:
					s = "Long"
				else:
					s = "Integer"
			
		return s
		
	def _get_cols(self,sql):
		''' 컬럼을 가져오는 함수.'''
		print 'con_str:' + self.con_str;
		cols = []
		try:
			self.con = cx_Oracle.connect(self.con_str)
			
	
			try:
				self.cursor = self.con.cursor()
		
				self.cursor.execute(sql)
				
				cols = self.cursor.description
			finally:
				self.cursor.close()
		finally:
			self.con.close()
		return cols
	def get_cols(self, sql):
		cols = self._get_cols(sql)

		s= ""
		first = util.First()
		for col in cols:
			#(name, t) = col[0],col[1]
			name = col[0]
			if not first.isFirst():
				s += ","
			s += name
		
		print s
		return s

	def get_vofields(self,sql):
		cols = self._get_cols(sql)
		
		mydict = util.load_file("dict.txt")
		
		s = ''
		for col in cols:
			(name, t,precision,scale) = col[0],col[1], col[4],col[5]
			tstr = self.get_type_str(t,precision,scale)
			camelstr = util.underscore_to_camel(name) + ' ;'
			hanname = util.eng_to_han_one(mydict, name)
			s += "private %-12s %-30s // %s\n" % (tstr, camelstr, hanname)
		return s;
		


class AgrixToolGTK:
	"""This is an Hello World GTK application"""

	def __init__(self):
		''' 클래스 초기화'''
		#Set the Glade file
		filename = "agrix_tool.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(filename)
		self.builder.connect_signals(self)
		
		# object 설정.
		self.tbSql 		= self.get_object('tbSql')
		self.tbColEng 	= self.get_object('tbColEng')
		self.tbColHan 	= self.get_object('tbColHan')
		self.tbLog 		= self.get_object('tbLog')
		
		# 굴림체로 폰트 설정함.
		self.set_font(self.get_object('tvLog'))
		self.set_font(self.get_object('tvSql'))
		self.set_font(self.get_object('tvColEng'))
		self.set_font(self.get_object('tvColHan'))
		
		self.popMenu = self.builder.get_object('popMenu')
		self.sqlMenu = self.builder.get_object('sqlMenu')
		

		
		win = self.builder.get_object('win');
		assert isinstance(win, gtk.Window)
		win.show_all()

	def _get_con_str(self):
		chk = self.builder.get_object('chkDb1')
		chk7 = self.builder.get_object('chkDb7')
		if(chk.get_active()):
			return "id/pass@host:1521/sid"
		if(chk7.get_active()):
			return "id/pass@host:1521/sid"
		return "id/pass@host:1521/sid"
			
		
		
	def set_font(self,o):
		#o.modify_font(pango.FontDescription('GulimChe 10'))
		o.modify_font(pango.FontDescription('Monospace 10'))
		

	def get_object(self,name):
		''' object 가져오기'''
		obj = self.builder.get_object(name)
		
		return obj
		
	def gtk_main_quit(self,widget):
		print "gtk_main_quit"
		gtk.main_quit()
		
		
	def on_tvLog_button_press_event(self, widget, e):
		''' 로그 마우스 클릭 이벤트 처리'''
		if e.button == 3 :
			self.popMenu.popup(None, None, None, e.button, e.time)
			return True
		
	def on_tvSql_button_press_event(self, widget, e):
		''' 로그 마우스 클릭 이벤트 처리'''
		if e.button == 3 :
			self.sqlMenu.popup(None, None, None, e.button, e.time)
			return True

	def on_btnTransText_clicked(self, widget):
		self.log("텍스트변환시작\n")
		tb = self.tbColHan
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())


		cols = util.split(s)
		msg =''
		for col in cols:
			camel = util.underscore_to_camel(col.upper())
			msg += col + '\n'
			msg += util.camel_to_underscore(col).upper() + '\n'
			msg += camel + '\n'
			msg += camel[0:1].upper() + camel[1:] + '\n'
			msg += '\n'
		self.log(msg);
		self.log('\n\n')
		#self.log(crud.mk_insert(cols))
		#self.log('\n\n')

	def on_btnSqlComment_clicked(self,widget):
		'''코멘트를 이용하여 SQL을 생성함.'''
		tb = self.tbSql
		mydict = util.load_file("dict.txt")
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		s = s.strip().upper()
		prefix = None
		if s.find('.') >= 0:
			(prefix, s ) = s.split('.')
		constr = self._get_con_str()
		self.log('연결문자열:' + constr + '\n')
		self.log('테이블명  :' + s + '\n')
		m = utildb.get_comment_info(constr, s.upper())
		#self.log(crud.mk_insert(cols))
		#self.log('\n\n')
		self.log(crud2.mk_insert2(mydict,m['dic'],m['cols']))
		self.log('\n\n')
		self.log(crud2.mk_update(mydict, m['dic'],m['cols']))
		self.log('\n\n')
		self.log(crud2.mk_select(mydict, m['dic'],m['cols'],prefix))
		self.log('\n\n')
		self.log(crud2.mk_select_insert(mydict, m['dic'],m['cols']))
		self.log('\n\n')
		
	def on_btnMkJoinSql(self,widget):
		'''코멘트를 이용하여 SQL을 생성함.'''
		tb = self.tbSql
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		s = s.strip().upper()
		msg = utildb.get_sql_equal_join(s)
		self.log(msg)
		
	def on_btnMkJoinRightPlusSql(self,widget):
		tb = self.tbSql
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		s = s.strip().upper()
		msg = utildb.get_sql_out_plus_join(s)
		self.log(msg)
		
	def on_miDatasetToVo_activate(self,widget):
		''' 데이터셋의 ColumnInfo 문자열을 VO문자열로 변경함.'''
		self.log("VO생성시작.\n")
		tb = self.tbSql
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		s = s.strip().upper()
		a = s.splitlines()
		msg = ''
		for l in a:
			m = re.search('"(\w+)"', l)
			w = m.group(1)
			w = util.underscore_to_camel(w)
			msg += "private String " + w + " ;\n" 
		self.log(msg)

	def get_tb_text(self,tb):
		'''텍스트버퍼 문자열 취득함수.'''
		return tb.get_text(tb.get_start_iter(), tb.get_end_iter())
	
		
	def on_miCodeFmt_activate(self, widget):
		'''코드 포맷팅 처리
		'''
		try:
			self.log("코드 포맷팅처리\n")
			txt = self.get_tb_text(self.tbColEng)
			if txt != None and len(txt.splitlines()) >= 1 :  (sep,) = txt.splitlines()
			if sep == None : return
			
			self.log("분리자 : " + sep + '\n')
			s = self.get_tb_text(self.tbSql)
			a = s.splitlines()
			toa = []
			maxlen = 0
			for l in a :
				t = l.split(sep)
				if len(t) > 1:
					tlen = len(t[0])
					if maxlen < tlen : maxlen = tlen
				toa.append(t)
			for l in toa:
				fmt = '{0:' + str(maxlen) + '}'
				if(maxlen == 0 ) : continue
				l[0] = fmt.format(l[0])
			s = ''
			for l in toa:
				s += sep.join(l) + '\n';
			self.log(s);
		except :
			tb = traceback.format_exc().decode('utf-8')
			self.log("********* ERROR ********* \n")
			self.log("도움말\n")
			self.log("영문1라인 : 분리자(seperator)\n")
			self.log("************************* \n")
			self.log(tb )
		
	def on_miSpaceCodeFmt_activate(self, widget):
		'''코드 포맷팅 처리
		'''
		try:
			self.log("스페이스 코드 포맷팅처리\n")
			txt = self.get_tb_text(self.tbColEng)
			#txt = txt.encode('string_escape')
			if txt != None and len(txt.splitlines()) >= 2 :  (gap, cnt) = txt.splitlines()
			if gap == None or cnt == None : return
			
			self.log("CNT is " + cnt + '\n')
			s = self.get_tb_text(self.tbSql)
			a = s.splitlines()
			#for i in range(len(a)):
			#	a[i] = a[i].encode('string_escape')
			toa = []
			gaps = gap.split(',')
			for i in range(len(gaps)):
				gaps[i] = int(gaps[i])

			cnt = int(cnt)
			maxa = [0] * cnt;
			
			for l in a :
				t = re.split(r'\s+',l, cnt)
				#for i in range(len(t)):
				#	t[i] = t[i].encode('string_escape')
				for i in range(cnt):
					if len(t) <= i: continue
					tlen = len(t[i])
					maxlen = maxa[i]
					if( maxlen < tlen ): maxlen = tlen + gaps[i]
					maxa[i] = maxlen
				toa.append(t)
			for l in toa:
				for i in range(cnt):
					maxlen = maxa[i]
					if(maxlen == 0 ) : continue
					fmt = '{0:' + str(maxlen) + '}'
					if len(l) <= i : continue
					l[i] = fmt.format(l[i])
			s = ''
			for l in toa:
				s += ''.join(l) + '\n';
			self.log(s);
		except :
			tb = traceback.format_exc().decode('euckr')
			self.log("********* ERROR ********* \n")
			self.log("도움말\n")
			self.log("영문1라인 : GAP1,GAP2,GAP3\n")
			self.log("영문2라인 : 스페이스분리 횟수(영문1라인의갯수와 동일)\n")
			self.log("************************* \n")
			self.log(tb )

		
	def on_btnMkJoinLeftPlusSql(self,widget):
		tb = self.tbSql
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		s = s.strip().upper()
		msg = utildb.get_sql_plus_out_join(s)
		self.log(msg)

	def rmSqlComment(self,sql):
		a = sql.splitlines()
		s = ''
		for l in a:
			t = re.sub(r'--.*$','',l) 
			s += re.sub(r'/\*.*\*/','',t) + '\n'
		return s

	def on_btnGetVoField_clicked(self,widget):
		#self._get_con_str();
		print ''' sql 을 이용하여 conlumn정보 가져오기'''
		#self.tbColEng.set_text('')
		#self.tbColHan.set_text('')
		

		bounds = self.tbSql.get_selection_bounds();
		if( len(bounds) < 2):
			print "no text is selected"
			self.log("no text is selected\n")
			tb = self.tbSql
			sql = self.tbSql.get_text(tb.get_start_iter(), tb.get_end_iter())
		else:
			sql = self.tbSql.get_text(bounds[0],bounds[1]);

		sql = self.rmSqlComment(sql)
		self.log('SQL : ' + sql + '\n');
		print sql

		try:
			dbCols = DbCols()
			dbCols.con_str = self._get_con_str()
			s = dbCols.get_vofields(sql)
			self.log(s)
		except :
			tb = traceback.format_exc().decode('euckr')
			self.log("********* ERROR ********* \n")
			self.log(tb )

			
	
	def on_btnGetCols_clicked(self,widget):
		print ''' sql 을 이용하여 conlumn정보 가져오기'''
		self.tbColEng.set_text('')
		self.tbColHan.set_text('')

		bounds = self.tbSql.get_selection_bounds();
		if( len(bounds) < 2):
			print "no text is selected"
			self.log("no text is selected\n")
			tb = self.tbSql
			sql = self.tbSql.get_text(tb.get_start_iter(), tb.get_end_iter())
		else:
			sql = self.tbSql.get_text(bounds[0],bounds[1]);
		sql = self.rmSqlComment(sql)
		self.log('SQL : ' + sql + '\n');
		print sql

		try:
			dbCols = DbCols()
			dbCols.con_str = self._get_con_str()
			cols = dbCols.get_cols(sql)
			
			tb = self.tbColEng
			assert isinstance(tb , gtk.TextBuffer)
			tb.set_text(cols)
			
			mydict = util.load_file("dict.txt")
			names = cols.split(',')
			hannames = util.eng_to_han(mydict, names)
			self.tbColHan.set_text(hannames)
		except :
			tb = traceback.format_exc().decode('euckr')
			self.log("********* ERROR ********* \n")
			self.log(tb)
			raise
			
		
	def on_btnGenSql_clicked(self,widget):
		''' SQL생성.'''
		tb = self.tbColEng
		mydict = util.load_file("dict.txt")
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		cols = util.split(s)
		#self.log(crud.mk_insert(cols))
		#self.log('\n\n')
		self.log(crud.mk_insert2(mydict, cols))
		self.log('\n\n')
		self.log(crud.mk_update(mydict, cols))
		self.log('\n\n')
		self.log(crud.mk_select(mydict, cols))
		self.log('\n\n')
		
		
	def on_btnGetDataset_clicked(self,widget):
		''' dataset 관련 정보 생성'''
		cols = self.get_cols_eng()
		s = dataset.get_column_info(cols)
		self.log(s)
		self.log("\n")
		
	def on_btnGetGrid_clicked(self,widget):
		''' 그리드 관련정보 생성'''
		colseng = self.get_cols_eng()
		colshan = self.get_cols_han()
		
		self.log(grid.get_columns_bylen(colseng))
		self.log("\n\n");
		self.log(grid.get_band_head(colshan))
		self.log("\n\n");
		self.log(grid.get_band_body(colseng))
		self.log("\n\n");
	
	def on_btnEngHanCmp_clicked(self,widget):
		engs = self.get_cols_eng()
		hans = self.get_cols_han()
		s = ""
		for i in range(len(engs)):
			s += "%s : %s\n" % (engs[i],hans[i] ) 
		
		self.log(s)
		
	def on_btnLogClear_clicked(self,widget):
		self.tbLog.set_text('')
		#self.tbColEng.set_text('')
		
	def on_btnGenChkCode_clicked(self,widget):
		''' 체크코드 생성 버튼 처리.'''
		mydict = util.load_file("dict.txt")
		tb = self.tbColHan
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		o = bindItemToVar.BindItemVar(s,mydict)
		self.log(o.getVarStr())
		self.log('\n\n')
		self.log(o.getChkStr())
		self.log('\n\n')
		self.log(o.getChkStr2())
		self.log('\n\n')
		self.log(o.getChkStr3())
		self.log('\n\n')

	def get_token(self,line):
		a = []
		b = []
		for c in line: a.append(c)
		a.reverse()
		for c in a:
			if c == ',': continue
			if c== '.' or c == ' ' or c == '\t' :
				break
			b.append(c)
		b.reverse()
		return "".join(b)
	def on_btnReOrderCol_clicked(self,widget):
		tb = self.tbColHan
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		a = s.splitlines()
		col = 0
		msg = ''
		self.log("순서정렬 버튼 클릭\n\n")
		for s in a:
			if(s.strip() == ''):
				continue
			
			s = re.sub(r'(col=)"\d+"', r'\1"' + str(col) + r'"',s)
			col +=1
			msg += s+'\n'
		self.log(msg)
		self.log('\n\n')
		
	def on_btnDefMap_clicked(self,widget):
		mydict = util.load_file("dict.txt")
		tb = self.tbColHan
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		a = s.splitlines()
		if( len(a) <2 ):
			a = util.split(s)
		msg = 'SQL의 SELECT구문을 이용하기 바랍니다\n\n'
		msg += 'BufMap defValMap = new BufMap();\n'
		msg += 'defValMap\n'
		for l in a:
			l = re.sub('/\*.*\*/','',l)
			l = l.strip()
			t = self.get_token(l)
			engname = t
			t = '"' + t + '"'
			hanname = util.eng_to_han_one(mydict,engname )
			msg += '\t\t.put(%-30s,"0")\t\t// %s\n' %(t,hanname)
		msg += '\t\t;\n'
		self.log("\n\n")
		self.log(msg)
		self.log("\n\n")

	def get_cols_eng(self):
		tb = self.tbColEng
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		cols = util.split(s)
		return cols
	
	def get_cols_han(self):
		tb = self.tbColHan
		assert isinstance(tb , gtk.TextBuffer)
		s = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
		cols = util.split(s)
		return cols
	
	def log(self,s):
		'''문자열을 로그버퍼에 추가함'''
		tb = self.tbLog
		assert isinstance(tb , gtk.TextBuffer)
		tb.insert(tb.get_end_iter(),s)
		
	def on_btnHelp_clicked(self,widget):
		self.log(myhelp.get_help())
		#d = gtk.FontSelectionDialog('테스트')
		#d.run()


if __name__ == "__main__":
	print "main....."
	hwg = AgrixToolGTK()
	gtk.main()
	
	print "end....."
