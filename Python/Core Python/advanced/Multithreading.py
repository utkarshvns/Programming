# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:51:02 2022

@author: utkar
"""

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):              # Inside thread class there is a method called run
        for i in range(5):
            print("Hello")
            sleep(1)  # thread sleeps for 1 sec

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

# t1.run()
# t2.run()

t1.start()          # Instead of run() call start() to get two different thread

sleep(0.2)          # To avoid collisions
t2.start()



t1.join()
t2.join()

# main thread will execute "Bye" only when t1 and t2 thereds complete their task and join

print("Bye")

