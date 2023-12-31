# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:29:41 2022

@author: utkar
"""

# type of Polymorphism
# method ovverloading and method overrriding

# method overloading is not in python - class with two method with same name and different parameters





class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a=None,b=None,c=None):  # Direct overloading is not supported i python
        s=0
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s


s1 =  Student(45, 54)


print(s1.sum(5,9,3))
print(s1.sum(5,9))
print(s1.sum(5))





