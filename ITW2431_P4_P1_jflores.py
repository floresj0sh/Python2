# Name:Josh Flores
# ITW 2431
# Project 4 Prob. 1
# File name: ITW2431_P4_P1_jflores.py
# MODIFIED: 09/16/2022
# PURPOSE: To find the sum of a list


print()
days = { 
    "Tuesday": "2",
    "Sunday": "7",
    "Monday": "1",
    "Thursday": "4",
    "Friday": "5",
    "Wednesday": "3",
    "Saturday": "6",
}

print(days)

marklist = sorted(days.items(), key=lambda x:x[1])
print("Output in ascending order: ")
for i, value in marklist:          #gets the value in the dictionary and prints them
    print(i, '=>',value)


marklist1 = sorted(days.items(), key=lambda x:x[1], reverse=True)
print("Output in descending order: ")
for i, value in marklist1:          #gets the value in the dictionary and prints them
    print(i, '=>',value)
