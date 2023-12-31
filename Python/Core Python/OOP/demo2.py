# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:21:17 2022

@author: utkar
"""

# Constructor variable and methods

class Computer:
    
    def __init__(self):
        self.name = "Navin"
        self.age = 26
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()

c1.age=30

c2 = Computer()

if c1.compare(c2):
    print("Same")
else:
    print("different")