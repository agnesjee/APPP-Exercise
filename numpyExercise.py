# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 07:57:50 2021

@author: ASUS
"""

import numpy as np

# Exercise 13
array1 = np.array ([1,23,456])
print(array1)
print(np.arange(9))
print(np.arange(10,20))
print(np.arange(100,111))

# Exercise 14
# Generate a 5x5 array of ints between 0 and 5
array2 = np.random.randint(5, size=(5,5))
print(array2)
array2[[0,4], :] = array2[[4,0], :]
print("Swapping first and last row:")
print(array2)

# Exercise 15
a = np.array([[0,2,4], [1,3,5]])
b = np.transpose(a)
print('Original','\n','Shape',a.shape,'\n',a)
print('Expand along columns:','\n','Shape',b.shape,'\n',b)

# Exercise 16
array3 = ([[10,30], [20,60]])
print("Mean value: ", np.mean(array3))










