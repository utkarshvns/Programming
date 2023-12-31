# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:53:24 2022

@author: utkar
"""

# Operator Overloading

# x=5
# y="tom"

# z=x+y


a = 5
b = 6

print(a+b)              #Synthetic Sugar

print(int.__add__(a, b))


# Magic methods for each operator



class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):            # Overloading '+' operator
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)
        return m3
    
    def __gt__(self,other):            # Overloading '>' operator
        r1 = self.m1 + self.m1
        r2 = other.m2 + other.m2
        if(r1>r2):
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(45, 69)
s2 = Student(78, 92)

s3 = s1 + s2            # Student.__add__(s1,s2)


print(s3.m1,s3.m2)



if(s1>s2):
    print("s1 wins")
else:
    print("s2 wins")


a = 9

print(a) # prints value and not address of object
print(a.__str__())      # Same as above



print(s1)
print(s1.__str__())











