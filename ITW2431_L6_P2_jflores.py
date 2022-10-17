# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 2
# File name: ITW2431_L6_P2_jflores.py
# MODIFIED: 9/27/2022
# PURPOSE: Take input as an interger, then with that input run the loop said amount of times to the second power and then putting it into a tuple.

lst1 = []       #creates list

number = int(input("Please enter the exponet number: "))        #ask for input

for i in range(1,number+1):     #loop starting at number 1 and ends one after the input
    lst1.append(2**i)       #appends value of i to the second power
print(tuple(lst1))

last = lst1[-1]         #gets last value of list

new_tuple = last *2     #multiplies last value of list by 2
lst1.append(new_tuple)      #adds value to list

print(tuple(lst1))      #prints list



lst1 = []       #reset the list
for i in range(1,number+1):         #same loop as before
    lst1.append(2**i)       #same equation as the last loop
    lst1.append(3**i)


print(tuple(lst1))      #prints out new list