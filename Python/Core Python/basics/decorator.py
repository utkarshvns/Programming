# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:17:17 2022

@author: utkar
"""

def div(a,b):
    print(a/b);
    

def smart_div(func):
    
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    
    return inner

div = smart_div(div)

div(2,4)
div(4,2)

