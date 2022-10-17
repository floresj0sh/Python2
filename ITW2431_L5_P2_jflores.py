# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 2
# File name: ITW2431_L5_P2_jflores.py
# MODIFIED: 9/19/2022
# PURPOSE: Find the biggest value in a list

string = input("Please type a string to count for letter occurrence: ")

dict = {}

for i in string:
    dict[i] = dict.get(i, 0) + 1
print(dict)
