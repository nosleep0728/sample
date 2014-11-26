'''
Created on 2014. 9. 17.

@author: dulee
'''

import sys
import pygtk
pygtk.require("2.0")
import gtk


class Snippets:
	"""This is an Hello World GTK application"""
	def __init__(self):
		filename = "snippets.glade"
		builder = gtk.Builder()
		builder.add_from_file(filename)
		builder.connect_signals(self)
		self.builder = builder
		
		win = builder.get_object('win')
		win.connect("destroy", gtk.main_quit)
		
		self.win = win

if __name__ == '__main__':
	print 'main'
	hwg = Snippets()
	gtk.main()
	print 'gtk end'