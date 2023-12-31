# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:01:33 2022

@author: utkar
"""

# method overriding- two method with asmae name and same arguments , one in parent one in child class


class A:
    
    def show(self):
        print("in A show")


class B(A):
    
    def show(self):
        print("in B show")


a1 = A()
a1.show()


b1 = B()
b1.show()



