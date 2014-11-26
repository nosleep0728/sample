# -*- coding: utf-8 -*-
'''
Created on 2014. 10. 15.

@author: dulee
'''



tmpl = '''
select {no} NO, '{name}' NM from dual union all'''



def gettbl(l, tmpl):
	a = l.split(' ')
	msg = ''
	for row in a :
		item = row.split(',')
		if( len(item) < 2): continue
		msg += tmpl.format(no=item[0],name=item[1])
	return msg


l = ''
for i in range(20):
	l += str(i) + ',name' + str(i) + ' '

print gettbl(l,tmpl)





s = '''
004001
004002
004003
004004
004005
004006
004007
004008
004009
004010
004011
004012
'''
a = s.splitlines()
m = ''
for i in a:
	m += "'" + i + "',"
print m
	