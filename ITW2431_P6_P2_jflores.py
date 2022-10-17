# Name:Josh Flores
# ITW 2431
# Project Prob. 1
# File name: ITW2431_P6_P2_jflores.py
# MODIFIED: 9/29/2022
# PURPOSE: 

clas = input("Please enter the courses you are taking in this semester: ")
prof = input("Please enter the professor's name for the course: ")

print()

lst = []
while clas!= "done":
    lst.append(clas)
    lst.append(prof)
    
    if clas == "done": 
        break
    clas = input("Please enter the courses you are taking in this semester: ")
    prof = input("Please enter the professor's name for the course: ")
    
print(tuple(lst))