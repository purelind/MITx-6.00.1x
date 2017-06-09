# -*- coding: utf-8 -*-
"""
Created on Fri Jun 8 2016

@author: Kevin
"""

s = "zyxwvutsrqponmlkjihgfedcba"
sub = ""
testsub = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        testsub += s[i]
    else:
        testsub = s[i]
    if len(testsub) > len(sub):
        sub = testsub
if len(sub) == 1:
    sub = s[0]
print("Longest substring in alphabetical order is: " + sub)


