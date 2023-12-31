# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:59:38 2022

@author: utkar
"""

# Generators

# def topTen():
    
#     yield 1
#     yield 2
#     yield 3     # return ends a function , yield does not
#     yield 4   # instead of return use yield keyword to make a function generator



# values = topTen()

# print(values.__next__())

# print(values.__next__())

# for i in values:
#     print(i)


def topTen():
    
    n= 1
    
    while(n<=10):
        sq = n*n
        yield sq
        n += 1


values = topTen()


for i in values:
    print(i)

#  Generators are useful while feching one record at a time from a db








