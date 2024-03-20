# Display's welcome message
# upon choice, ask for password
# Ask's what user wants to do
# check the correctness of the password
# based on user's choice, runs AgeCalculator function
# or Calculator function
# also integrates another function to handle the password reset option


def auth():
    print("Welcome Favourite Human!")
    password = input("Enter password: ")
    
    if password == '1234':
        print("Choose from the options below")
        print("Press 1 for AgeCalculator\nPress 2 for Calculator")
        
        choice = input("Enter choice: ")

        if choice == '1':
            # Calls AgeCalculator function
            AgeCalculator()
        
        elif choice == '2':
            # Calls Calculator function
            Calc()
        
        else:
            print("Invalid response")
    else:
        print("Looks like you've forgotten your password")
        print("Reset Password?")
        exit()

def AgeCalculator():
    print("Hello, Human!")
    DOB = input("Type in your year of birth:")
    AGE = (2024-int(DOB))
    print("That's great, you're", AGE, "years old!")
    print("Have a wonderful day!")

# Define the Calculator function
def Calc():
    print("Calculator")
    print("Type 'quit' to exit")

    run = True
    while run:
        equation = input("Enter equation:")
        if equation == 'quit':
            run = False  
        else:
            previous = eval(equation)
            print("Your answer is:", previous)

while True:
    auth()

    option = input("Would you like anything else? (yes/no): ")
    if option.lower() == 'no':
        print("Now Exiting Program........Byebye!!")
        break
    else:
        print("Returning to program")