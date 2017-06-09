# -*- coding: utf-8 -*-
"""
Created on Fri Jun 8 2016

@author: Kevin
"""

s = "abdcd"
count = 0

for vowelsItem in s:
    if vowelsItem in "aeiou":
        count += 1

print("Number of vowels: " + str(count))