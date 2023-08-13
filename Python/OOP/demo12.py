# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:19:20 2022

@author: utkar
"""

from abc import ABC,abstractmethod

#Abstract class - has at least one abstarct method in it

class Computer(ABC):             # python don't have abstarct classes by default
    @abstractmethod
    def process(self):      # abstract method, only decleration and no definition
        pass

# an abstract class can't have an object


class Laptop(Computer): # class inheriting abstract class implements the method otherwise it will also be an asbstract class
    def process(self):
        print("a laptop")


class Whiteboard(Computer()):
    def write(self):
        print("it's writing")


    
class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()


# com = Computer()
# com.process()


com1 = Laptop()

com1.process()


com2 = Whiteboard()



prog1 = Programmer()

prog1.work(com1)


prog1.work(com2)