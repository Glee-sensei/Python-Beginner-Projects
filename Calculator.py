# Display a welcome message
# initialise a variable to store previous number as 0
# another variable run = True
# set quit instruction
# create a custom function
# set run and previos as global variables
# set a variable that collects user input
# if statement to handle evaluation logic and else to operationalise the quit instruction
# while loop to iterate the entire function
# call your function

import re
print("Calculator")
print ("type 'quit' to exit")

previous = 0
run = True

def Calc():
    global previous
    global run
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        previous = eval(equation)
        print("Your answer is:", previous)

while run:
    Calc()