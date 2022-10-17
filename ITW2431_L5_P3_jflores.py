# Name:Josh Flores
# ITW 2431
# Lab 5 Prob. 3
# File name: ITW2431_L5_P3_jflores.py
# MODIFIED: 9/19/2022
# PURPOSE: Given a dictionary print out key and values in descending order.

dict = {'item1': 105, 'item2':25, 'item3': 31, 'item4':65, 'item5': 234}        #dictionary

dict_sort = sorted(dict.items(), key=lambda x:x[1], reverse=True)       # sorted dictionary
print(dict_sort)        #print dictionary