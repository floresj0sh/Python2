# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 1
# File name: ITW2431_L5_P1_jflores.py
# MODIFIED: 9/19/2022
# PURPOSE: Take more than 3 inputs into a dictionary as values, until input equals 0. Put inputs into dictionary and put it into numbered order.


dict = {}

for i in range(3):      #initial input has to be greater than 3
    dict[i+1] = int(input("Please enter the #" + str(i+1) + " int number until done: "))

i = 4 # taking numbers till done is entered
n = input("Please enter the #" + str(i) + " int number until done: ")   
while n!="done":        #when n or input is equal to done breaks the loop
    dict[i] = int(n)
    i+=1
    n = input("Please enter the #" + str(i) + " int number until done: ")

print(dict) # printing the dictionary

values = list(dict.values())        # sorting values of the dictionary
values.sort()
values = values[::-1]       # prints the values in reverse

# printing output
print("3 largest values are:", values[0], values[1], values[2]);