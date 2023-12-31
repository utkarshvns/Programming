# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 14:35:55 2022

@author: utkar
"""

# inner class- when you know a class will not be used for anything else 
# than for a given class you can create an inner class.

class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop:
        
        def __init__(self):
            self.brand ='HP'
            self.cpu = 'i5'
            self.ram = 8
            
        def show(self):
            print(self.brand,self.cpu,self.ram)            
    

s1 = Student("Utkarsh", 17)
s2 = Student("Raj", 11)

s1.show()
# s1.Laptop().show()

# s1.lap.brand

lap1 = s1.lap
lap2 = s2.lap

lap3 = Student.Laptop()

# you can create object of inner class inside outer class  or 
#you can create object of inner class  outside of outer class given you use outer class name to call it  


print(id(lap1))
print(id(lap2))