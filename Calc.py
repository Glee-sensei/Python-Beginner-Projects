import sympy

def Calc():
    print("Welcome, human! What'll you like to do?")
    choice = ""
    while choice not in ['1', '2']:
        choice = input("Select 1 for age calculator and 2 for maths calculator: ")

    if choice == '1':
        Age_Calc()
    elif choice == '2':
        Math_Calc()

    else:
        print("Please select a valid option")

def Age_Calc():
    print("Oka eri sama!")
    currentYear = int(input("What year is it? "))
    DOB = int(input("Enter DOB: "))
    Age = currentYear - DOB
    print("Yo, Human! you're", Age, "year old")


def Math_Calc():
    print("Heyo! Let's do some maths, shall we!")
    print("Type 'quit' to exit program")

    previous = 0
    realtime = True

    while realtime:
        equation = input("Type in an equation: ")
        if equation.lower() == 'quit':
            realtime = False
        else:
            try:
                previous = sympy.sympify(equation)
                print("Your answer is", float(previous))
            except (sympy.SympifyError, TypeError) as e:
                print("Invalid response. Please try again.")
Calc()