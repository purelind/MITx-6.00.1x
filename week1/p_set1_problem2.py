# -*- coding: utf-8 -*-
"""
Created on Fri Jun 8 2016

@author: Kevin
"""


s = "bobbobob"
count = 0

for i in range(len(s)-2):
    if s[i:i+3] == "bob":
        count += 1

print("Number of times bob occurs is: " + str(count))
