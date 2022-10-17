# Name:Josh Flores
# ITW 2431
# Lab 3 Prob. 2
# File name: ITW2431_L3_P1_jflores.py
# MODIFIED: 9/1/2022
# PURPOSE: Takes inputs as numbers and adds them to a list. Once input reads 'done' prints out the max and min numbers in the list

num_list=[]     #creates list
while True:
    number=input("Enter a number:")     #ask for number input
    if number == "done":        #if the number input = done it breaks the loop
        break
    else:
        num_list.append(float(number))      #adds the number input into the list and continues the loop
        continue
print("Maximum:",max(num_list))         #prints the highest value in the list
print("Minimum:",min(num_list))         #prints the lowest value in the list
