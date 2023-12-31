# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:50:16 2022

@author: utkar
"""

# Types of Variables

class Car:
    
    wheels = 4 #Class variable
    
    def __init__(self):
        self.mil = 10           #instance variables
        self.com = "BMW"
        


c1 = Car()
c2 = Car()


c1.mil = 8

Car.wheels = 5


print(c1.com,c1.mil, c1.wheels)

print(c2.com,c2.mil, c2.wheels)