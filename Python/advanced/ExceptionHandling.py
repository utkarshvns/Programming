# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:17:03 2022

@author: utkar
"""

a=5
b=2

try:
    print("resource open")
    print(a/b)
    k = int(input("Eneter a number:"))
except ZeroDivisionError as e:
    print("can't devide by 0", e)
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("something went wrong", e)
finally:
    print("resource closed")


# Exception class can handle all exceptions


print("Bye")