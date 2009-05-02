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
        thegcd = self.gcd(num,dem)
        self.num = num/thegcd
        self.dem = dem/thegcd
    
    def gcd(self,num1, num2):
        """gcd helper function"""
        gcd = 1
        for i in range(2,abs(num1)+1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i
        return gcd
    
    def __unicode__(self):
        return str(self.num) + "/" + str(self.dem)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.dem)
    
    def __add__(self, other):
        other = self.getOther(other)
        sum = self.num*other.dem + other.num*self.dem
        newdem = other.dem*self.dem
        return Rational(sum,newdem)
        
    def __sub__(self, other):
        other = self.getOther(other)
        sub = sum = self.num*other.dem - other.num*self.dem
        newdem = other.dem*self.dem
        return Rational(sub,newdem)
    
    def __mul__(self, other):
        return Rational(self.num*other.num,self.dem*other.dem)
    
    def __div__(self, other):
        other = Rational(other.dem,other.num)
        return self*other
    
    def toFloat(self):
        return (self.num+0.0)/self.dem
    
    def getOther(self,other):
        """didn't quite think through how to treat it if not rational. 
        Problem didn't specify, so I just accept ints or Rational"""
        toadd = other
        if(other.__class__ == int):
            toadd = Rational(other,1)
        if(toadd.__class__ != Rational):
            raise
        return toadd
    


#expected to run as shell script
if __name__ == "__main__":
    test = Rational(3,2)
    test2 = Rational(1,6)
    new =  test + test2
    print new
    print new.toFloat()
    new2 = test - test2
    print new2
    print new2.toFloat()
    new3 = test * test2
    print new3
    print new3.toFloat()
    new4 = test / test2
    print new4
    print new4.toFloat()
