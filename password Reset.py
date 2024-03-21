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

reset()