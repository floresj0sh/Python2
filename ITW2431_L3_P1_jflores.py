# Name:Josh Flores
# ITW 2431
# Lab 3 Prob. 1
# File name: ITW2431_L3_P1_jflores.py
# MODIFIED: 9/1/2022
# PURPOSE: Count how many lines start with From then prints out email address.

print()     #prints blank line
count=0     #sets count to 0
fhand = open("mbox-short (1).txt")      #opens file
for line in fhand:      #for loop to read through line
    line = line.rstrip()
    if not line.startswith('From ') : continue      #if line starts with from continue
    words = line.split()        #splits the words in line
    print(words[1])     #prints out the 2 words in the line
    count=count+1       #adds 1 to the count
print(line)     #prints the variable
print("There were",count, "lines in the file with From as the first word")      #prints how many times the loop ran
print()