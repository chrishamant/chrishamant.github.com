#!/usr/bin/env python
# encoding: utf-8
"""
CS340 Assignment #1
asg1.py
Chris Hamant
chris@hamant.net
w007csh

Simple program that just does what the comments say. More comments than code!
"""

def perfect(number):
    #just explicity test for these special cases as filter/reduce below don't deal with them
    if number < 2: # 0,1,or neg numbers
        return False
    
    #filters range/list of 1 to (n/2)+1 into a list of factors of 'number'
    factors = filter(lambda x:number%x==0,range(1,(number/2)+1))
    #performs summation of factors list and tests whether is equal to number (defn of 'perfect number')
    return reduce(lambda x,y:x+y, factors) == number


#expected to run as shell script
if __name__ == "__main__":
    #per problem, filters list of 0-1000 into list of perfect numbers
	perfectsinrange = filter(perfect, range(1000))
	print perfectsinrange

