# Name:Josh Flores
# ITW 2431
# Project 4 Prob. 2
# File name: ITW2431_P4_P2_jflores.py
# MODIFIED: 09/16/2022
# PURPOSE: Create a dictionary, then ask for an input, with that input number tells you how many values to add.


old_dict = {            #created dictionary
    0: 10,
    1: 20,

}

print("Old dictionary is: ",old_dict)         #prints the dictionary

num = int(input("How many runs do you want to add items for dictionary? "))     #ask for a number input

key=2       #sets key value to 2

for i in range(num):        #for loop to run as many times as the int input
    old_dict[key] = (key+1) *10         #dictionary key is added to one and the value is the key times 10
    key+=1          #adds 1 to the key
    print("After the #"+str(i+1), "run", "The New Dictionary is: ",old_dict)        #prints the statements