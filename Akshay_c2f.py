# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 10:44:41 2017

@author: kua
"""

def centfar(Centi):
  Faren = (Centi*1.8) + 32
  return Faren

print("cent","faren")
for i in range(-100,100,10):
  if i == centfar(i):
    print(i,centfar(i))
    