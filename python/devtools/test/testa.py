# -*- coding: utf-8 -*-
'''
Created on 2014. 11. 20.

@author: dulee
'''




class A:
	def __init__(self):
		print "inited..."
		self.a = 0

	def __add__(self,y):
		self.a += y.a
		return self
	
	def __str__(self):
		return str(self.a)
	
	
a = A()
a.a = 3
b = A()

b.a = 2
print a+b


class P:
	def __init__(self,name):
		self._name = name
	def getName(self):
		print 'fetch...'
		return self._name
	
	def setName(self,value):
		print 'change...'
		self._name = value
	
	def delName(self):
		print 'remove...'
		del self._name
	
	name = property(getName, setName, delName,"name property docs")
	print 'aaa'
	xxx = None
	
bob = P('bob')
print bob.name
print bob.xxx






