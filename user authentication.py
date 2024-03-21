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
        
        while True:
            choice = input("Enter choice: ")

            if choice == '1':
                # Calls AgeCalculator function
                AgeCalculator()
        
            elif choice == '2':
                # Calls Calculator function
                Calc()
        
            elif choice == 'exit':
                break

            else:
                print("Invalid response")
                print("pick from provided options")
    else:
        print("Looks like you've forgotten your password")
        option = input("Reset Password? (yes/no): ")
        if option.lower() == 'yes':
            # Calls reset function
            reset() 

        else:
            print("Refer to mail for other recovery options")
            exit()

# Define the AgeCalculator function
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
            print(equation,"=", previous)

# Define the password reset function
def reset():
    print("How could you've forgotten?")
    print("Luckily, I gotcha covered!!!!")
    answer = input("What's your favourite food?\n")
    if answer.lower() == 'beans':
        while True:  # Loop until password confirmation is successful or user exits
            new = input("CREATE NEW PASSWORD: ")
            confirm = input("CONFIRM PASSWORD: ")
            if new != confirm:
                print("Password match failed!!")
                choice = input("Do you want to try again? (yes/no): ")
                if choice.lower() == 'no':
                    print("Exiting password reset process.")
                    break  # Exit the loop if user chooses not to try again
            else:
                print("Password Reset Successful!!")
                break  # Exit the loop if password reset is successful
    else:
        print("Wrong input, refer to mail for more recovery options")

while True:
    auth()

    option = input("Would you like anything else? (yes/no): ")
    if option.lower() == 'no':
        print("Now Exiting Program........Byebye!!")
        break
    else:
        print("Returning to program")