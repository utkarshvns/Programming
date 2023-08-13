# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 12:02:36 2022

@author: utkar
"""

# Types of Methods


class Student:
    
    school = "IIMC"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):     #instance method can be accessor(access value) or mutators(mute values)
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):  #accessor
        return self.m1
    
    def set_m1(self,value):  #mutator
        self.m1 = value
        
    @classmethod
    def getSchool(cls):     # class method
        return cls.school
    
    @staticmethod
    def info():    # Static method , when no class/instance variable is used
        print("This is student class ....")




s1 = Student(25, 32, 45)
s2 = Student(98, 89, 56)

print(s1.avg())

print(Student.getSchool())

Student.info()



