# Name:Josh Flores
# ITW 2431
# Lab 4 Prob. 1
# File name: ITW2431_L4_P1_jflores.py
# MODIFIED: 9/15/2022
# PURPOSE: Create a dictionary then take inputs and print birthdays of inputs based on the dictionary

birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",          #creates birthday dictionary
    "Ada Lovelace": "12/10/1815",
}



def question():     #defines questions functions
    print("Welcome to the birthday query. We know the birthday of:", "\n")

    for i, value in birthdays.items():          #gets the value in the dictionary and prints them
        print('==>',i)
    date = input("Who's birthday do you want to look up? ")      #takes input
    if date in birthdays:           #if input is in birthdays dictionary print the statement
        print(date+"'s birthday is", birthdays[date]+'.')
    else:           #if the input is not in the dictionary print this
        print()
        print("Sorry, we don't have", date, "birthday.", "\n")    
question()          #calls the function

continue_loop = input("Do you want to continue (Y/N?)")            #takes input to continue
print()
continue_yes = ['Y','y']        #list of values
if continue_loop in continue_yes:       #if the input is in the list call the function
    question()
    
print("Add more birthdays to the dictionary", "\n")
print() #prints blank lines
print()
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",          #creates birthday dictionary
    "Ada Lovelace": "12/10/1815",
    "Charles Chaplin": "4/16/1889",
    "Franklin Delano Roosevelt": "1/30/1882",
    
}

question()
continue_loop = input("Do you want to continue (Y/N?)")         #takes input to continue
continue_yes = ['Y','y']        #list of values
if continue_loop in continue_yes:       #if the input is in the list call the function
    question()