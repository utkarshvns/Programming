# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:04:15 2022

@author: utkar
"""

# import calc

# print(calc.add(2, 5))



# from calc import *

# c = add(1,2)

# print(c)


from calc import add


def fun1():
    add(2,4)
    print("from fun1")

def fun2():
    print("from fun2")


def main1():
    fun1()
    fun2()

main1()
