# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:13:08 2022

@author: utkar
"""

# read file

f = open('MyData.txt','r')

# print(f.read())

# print(f.readline(4))

# print(f.readline(),end="")
# print(f.readline())


# write

f1 = open('abc.txt','w')

# f1.write("Laptop")

# append

# f1 = open('abc','a')

# f1.write("Mobile")


# read from a file and write to other

for data in f:
    f1.write(data)


# reading and writing an image as binary file


f2 = open('img.jpg','rb')

f3 = open('myImg.jpg','wb')

for i in f2:
    f3.write(i)











