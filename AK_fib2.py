# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 00:54:48 2017

@author: kua
#"""
def fib(x):
    a=1
    b=1
    print(a)
    print(b)
    for i in range(x):
        c=a+b
        print(c)
        a=b
        b=c
    

fib(10)

        