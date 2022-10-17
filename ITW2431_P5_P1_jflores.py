# Name:Josh Flores
# ITW 2431
# Project 5 Prob. 1
# File name: ITW2431_P5_P1_jflores.py
# MODIFIED: 09/22/2022
# PURPOSE: Read a text file and put the contents into a dictionary and average of the contents

fhand = open("studentGrade.txt")
dict = {}


for line in fhand:
    line = line.rstrip(" ")
    for word in line:
        dict[word] = dict.get(word, 0)
print(dict)