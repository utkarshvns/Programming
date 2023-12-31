# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:35:18 2022

@author: utkar
"""

num=5

id(num)

type(num)

num=6+5j

print(type(num))

a=5

b=float(a)

print(b)

k=6
c= complex(b,k)

print(c)
print(type(c))


check = a<k


print(type(check))

int(True)


#Sequence

my_list=[1,2,3]
my_tuple= (1,5,8)
my_set = {1,8,6}
my_string = "Awesome"
my_range= range(1,5)

type(my_list)
list(range(2,10,2))


# Dict

my_dictionary={"a":45,"b":"tom"}

my_dictionary.keys()
my_dictionary.values()


my_dictionary['a']
my_dictionary.get('a')

