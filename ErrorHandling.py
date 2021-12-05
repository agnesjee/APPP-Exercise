# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:16:51 2021

@author: ASUS
"""

def do_stuff_with_number(n):
    print(n)
    
the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
        
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)