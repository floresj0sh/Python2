# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 2
# File name: ITW2431_L7_P1_jflores.py
# MODIFIED: 10/05/2022
# PURPOSE: Take a string and print out how many times a letter occurs

string = input("The string is: ")

dict = {}

tup = print("The converted tuple is: ",tuple(string))



for x in string:
    if not dict.get(x):
        dict[x] = 1
    else:
        dict[x] += 1

for x in dict:     #for loop going through the string
    if dict[x]>1:               #puts each letter of the string the dictionary and adds 1 to the value.

        print("The repeated letter "\"+str(x)+"\" has "+str(dict[x])+" occurrences in tuple")    
    