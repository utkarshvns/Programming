# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:40:07 2022

@author: utkar
"""

# nums = [5,3,9,2]

# it = iter(nums)   # convert list into an iterator


# print(it.__next__())

# print(it.__next__())

# print(next(it))



# create own iterator class


class TopTen:
    
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration  # raising exception to stop for loop.for loop internally handles it


values = TopTen()


print(values.__next__())

# for loops internally used __next__()

for i in values:
    print(i)









