# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 28.

@author: dulee
'''
import re

class First(object):
	first = True
	def isFirst(self):
		if(self.first):
			self.first = False
			return True
		return False

def split(s):
	if(s.find('\t') >= 0):
		rows = s.split('\t')
	elif s.find(';') >= 0:
		rows = s.split(';')
	else:
		rows = s.split(',')
	return rows


def get_col_str(l):
	s = ""
	for i in range(l):
		if(i==0):
			pass
		else:
			s = s + ","
		s = s + "col" + str(i + 1)
	return s

def rm_last_one_char(s,c):
	i = s.rfind(c)
	if( i < 0):
		return s
	ret = s[:i] + ' ' +s[i+1:]
	return ret
	

def get_size_str(l):
	s = ""
	for i in range(l):
		if(i==0):
			pass
		else:
			s = s + ","
		s = s + "100"
	return s


def camel_to_underscore(name):
	''' camel case를 under score형태로 변경하는 함수. '''
	s1 = re.sub(r'(.)([A-Z][a-z]+)',r'\1_\2',name)
	return re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',s1).lower()

_under_pat = re.compile(r'_([a-z])')
def underscore_to_camel(name):
	''' under score형태의 문자열을 camel표기법으로 변경하는 함수. '''
	name = name.lower()
	return _under_pat.sub(lambda x: x.group(1).upper(), name)




def load_file(filename):
	''' KEY 탭 값 의 파일을 읽은 후, dictionary 를 만들어 리턴하는 함수. 
	'''
	d = {}
	f = open(filename)
	for line in f:
		line = line.strip()
		#print line
		if( line == "") :
			continue
		arr = line.split("\t")
		if len(arr) < 2:
			continue
		(key,value) =arr
		#d[key] = unicode(value,'cp949')
		key = key.strip().upper()
		if d.has_key(key):
			continue
		d[key] = value.strip()
	f.close()
		
	return d

def eng_to_han(mydict, names):
	''' '_'가 포함된 영문 문자열을 한글문자열로 변경하는 함수. 
	'''
	s = ""
	
	first = First()
	for name in names:
		if not first.isFirst():
			s += ","
		name = name.upper()
		words = name.split('_')
		firstword = First()
		for w in words:
			if not firstword.isFirst():
				s += " "
			w = w.upper()
			v = w
			if( mydict.has_key(w) ):
				v = mydict[w]
			s += v 
	return s

def eng_to_han_one(mydict, name):
	''' '_'가 포함된 영문 문자열을 한글문자열로 변경하는 함수. 
	'''
	s = ""
	name = name.upper()
	words = name.split('_')
	firstword = First()
	for w in words:
		if not firstword.isFirst():
			s += " "
		w = w.upper()
		v = w
		if( mydict.has_key(w) ):
			v = mydict[w]
		s += v 
	return s


