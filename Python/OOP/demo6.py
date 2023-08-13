# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:33:38 2022

@author: utkar
"""

# Inheritence


class A:
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")

class C(B):
    def feature5(self):
        print("Feature 5 working")

class D:
    def feature6(self):
        print("Feature 6 working")

class E(A,D):
    def feature6(self):
        print("Feature 7 working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()
b1.feature3()

c1 = C()            # Multilevel inheritence
c1.feature1()
c1.feature3()
c1.feature5()


e1 = E()            # Multiple inheritence

e1.feature1()
e1.feature6()

