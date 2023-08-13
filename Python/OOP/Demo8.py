# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:35:16 2022

@author: utkar
"""

# polymorphism  (loose coupling, dependency injection, interface)
    # Duck Typing
    # operator overloading
    # method overloading
    # method overriding




# Duck typing


class PyCharm:
    
    def execute(self):
        print("Compiling")
        print("Running")


class Spyder:
    
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()
        

ide1 = PyCharm()
ide2 = Spyder()


lap1 = Laptop()

lap1.code(ide1) 

# the code function doesn't depend on type of ide as long as it has an execute function

lap1.code(ide2)



