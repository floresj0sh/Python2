# Name:Josh Flores
# ITW 2431
# Project Prob. 1
# File name: ITW2431_P7_P1_jflores.py
# MODIFIED: 9/29/2022
# PURPOSE: 

string = input("Please enter a string: ")

list=[]

i = string.split(' ')
list.append(i)
print(list)

for i in list:
    if i in p:
        continue
    a=list.count(i)
    if(a>1):
        p[i]=a;
for key in p:
    print("The repeated word",key,"has",p[key],"occurances in tuple")

