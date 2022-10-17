# Name:Josh Flores
# ITW 2431
# Lab 8 Prob. 1
# File name: ITW2431_L8_P1_jflores.py
# MODIFIED: 10/10/2022
# PURPOSE: 

Str1 = "ABCDEFabcdef123450"

Str2 = "ABCDEF;abcdef'1234!50"

Str3 = "*&%@#!}{"


list=[]

for i in Str1:
    if i is int or char:
        print("This string doesn't contain any non_alpanumeric chars")
    else:
        list.appened(i)
print(list)