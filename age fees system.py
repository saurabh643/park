# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:28:47 2020

@author: Saurabh
"""

print("Welcome to hamara park.\n")
print("please enter your age")
age =int(input())

if age<=4:
    print("Your admission cost is $0.")
elif age<=18:
    print("Your admission cost is $25.")
    print("Pay your fees to enter in","hamara park")
else:
    print("Your admission cost is $40.")
    print("Pay your fees to enter in","hamara park")