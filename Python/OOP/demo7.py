# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:48:37 2022

@author: utkar
"""

# Constructor in inheritence and Method resolution order (MRO)


class A:
    
    def __init__(self):
        print("in A init")
        
    def feature1(self):
        print("Feature 1-A working")
        
    def feature2(self):
        print("Feature 2 working")


class B(A):
    
    def __init__(self):
        print("in B init")
        
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")
    
        
class C(A):
        
    def feature5(self):
        print("Feature 5 working")  
    
class D(A):
    
    def __init__(self):
        super().__init__()
        print("in D init")
        
    def feature6(self):
        print("Feature 6 working")


class E:
    
    def __init__(self):
        super().__init__()
        print("in E init")
        
    def feature7(self):
        print("Feature 7 working")

class F(A,E):
    
    def __init__(self):
        super().__init__()
        print("in F init")
        
    def feature8(self):
        print("Feature 8 working")

class H:
            
    def feature1(self):
        print("Feature 1-H working")
        
class I(H,A):            
    def feature9(self):
        print("Feature 9 working")
    
    def feat1(self):
        super().feature1()
    def feat2(self):
        super().feature2()


a1 = A() # call constructor

b1 = B() # call child constructor

c1 = C() # call parent constructor

d1 = D() # call both

f1 = F() #MRO calling constructor from left to right order gievn in case of multiple inheritence 




# Not only init, MRO is applicable for any other method when methods have same name in different classes

i1 = I()
i1.feature1()
i1.feat1()
i1.feat2()


