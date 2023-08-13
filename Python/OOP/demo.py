# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:50:41 2022

@author: utkar
"""

# init method constructor

class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is ", self.cpu ,self.ram)


com1 = Computer('i5',16)
com2 = Computer('ryzen 3',8)

# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()

print(type(com1))       