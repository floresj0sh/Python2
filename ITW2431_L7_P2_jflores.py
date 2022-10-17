# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 2
# File name: ITW2431_L7_P2_jflores.py
# MODIFIED: 10/05/2022
# PURPOSE: Create a tuple and with the tuple sort the items from least to greatest and do it backwords

dict = {'item4':65, 'item2':25, 'item5': 234, 'item3': 31, 'item1': 105}



dict_sort1 = sorted(dict.items(), key=lambda x:x[1])   # sorted dictionary


for i, value in dict_sort1:          #gets the value in the dictionary and prints them
    print("The print result in ascending order: ",i, '=>',value)


print()

dict_sort = sorted(dict.items(), key=lambda x:x[1], reverse=True)       # sorted dictionary


for i, value in dict_sort:          #gets the value in the dictionary and prints them
    print("The print result in descending order: ",i, '=>',value)