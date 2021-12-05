# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Exercise 1
print("Welcome to Advanced Python Programming Professional.")

# Exercise 2
mystring = "hello"
myfloat = 10.0
myint = 20

print(mystring)
print(myfloat)
print(myint)

# Exercise 4
s = "I Love Advanced Python Programming Professional"

# Find the length of the string s
length = len(s)
print("The length of the string s is " + str(length))

# Find the first occurence of "a"
index = s.find("a")
print("The index of the first occurence of 'a' is " + str(index))

# Count the occurence of "a" in string s
counter = s.count("a")
print("The character 'a' has appeared " + str(counter) + " times in string s")

print(s[:5])
print(s[5:10])
print(s[12])
print(s[1::2])
print(s[-5:])
print(s.split(" "))



