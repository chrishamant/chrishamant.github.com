#!/usr/bin/env python
# encoding: utf-8
"""
CS340 Assignment #3
asg3.py
Chris Hamant
chris@hamant.net
w007csh

Tkinter Calculator
"""

from Tkinter import *

class Calc(Frame):
	"""Simple class to trampoline a string input from user to eval()"""
	
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Calculator")
		
		#create main display using Tkinter type (makes it easy to observe)
		self.display = StringVar()
		self.display.set("3 + 3")
		self.displayBox = Message(self,relief=RAISED, textvariable=self.display)
		self.displayBox.grid(columnspan=3,sticky=EW)
		
		
		#I didn't see a reason to keep a reference to all the buttons
		#rows of 'functions'
		Button(self, text= "C", command = self.clearDisplay).grid(row=1,column=0)
		Button(self, text= "/", command = lambda: self.addToDisplay(" / ")).grid(row=2,column=0)
		Button(self, text= "*", command = lambda: self.addToDisplay(" * ")).grid(row=2,column=1)
		Button(self, text= "-", command = lambda: self.addToDisplay(" - ")).grid(row=2,column=2)
		Button(self, text= "+", command = lambda: self.addToDisplay(" + ")).grid(row=1,column=1)
		Button(self, text= "=", command = self.evalToDisplay).grid(row=1,column=2)
		
		#I should make this a loop
		Button(self, text= "9", command = lambda: self.addToDisplay("9")).grid(row=3,column=0)
		Button(self, text= "8", command = lambda: self.addToDisplay("8")).grid(row=3,column=1)
		Button(self, text= "7", command = lambda: self.addToDisplay("7")).grid(row=3,column=2)
		Button(self, text= "6", command = lambda: self.addToDisplay("6")).grid(row=4,column=0)
		Button(self, text= "5", command = lambda: self.addToDisplay("5")).grid(row=4,column=1)
		Button(self, text= "4", command = lambda: self.addToDisplay("4")).grid(row=4,column=2)
		Button(self, text= "3", command = lambda: self.addToDisplay("3")).grid(row=5,column=0)
		Button(self, text= "2", command = lambda: self.addToDisplay("2")).grid(row=5,column=1)
		Button(self, text= "1", command = lambda: self.addToDisplay("1")).grid(row=5,column=2)
		
		#pack and display
		self.grid()
	
	def addToDisplay(self,token):
		"""Instance method to add new token to display"""
		newtext = self.display.get() + token.strip()
		self.display.set(newtext)
		
	def clearDisplay(self):
		"""Instance method to clear the display variable"""
		self.display.set("")
		
	def evalToDisplay(self):
		"""Instance method to evaluate exising expression and update display"""
		text = self.display.get()
		if text != "":
			self.display.set(eval(text))


#expected to run as shell script
if __name__ == "__main__":
	Calc().mainloop()


