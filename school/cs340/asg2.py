#!/usr/bin/env python
# encoding: utf-8
"""
CS340 Assignment #2
asg2.py
Chris Hamant
chris@hamant.net
w007csh

Rational Class and driver program to test
"""

class Rational:
    """Class to represent rational numbers"""
    
    def __init__(self,num=1,dem=1):
        numneg = demneg = False
        if num < 0:
            numneg = True
        if dem < 0:
            demneg = True
        if num == 0 or num == 1:
            self.num = num #no more processing
        if dem == 0 or dem == 1:
            self.dem = dem
        
        factorsOfNum = filter(lambda x:num%x==0,range(1,(num/2)+1))
        factorsOfDem = filter(lambda x:dem%x==0,range(1,(dem/2)+1))
        print factorsOfNum
        print factorsOfDem
        self.num = num
        self.dem = dem
        
        
    def __unicode__(self):
        return str(self.num) + "/" + str(self.dem)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.dem)
    
    def __add__(self, other):
        pass
    
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        pass
    
    

#expected to run as shell script
if __name__ == "__main__":
    test = Rational()
    print test  

