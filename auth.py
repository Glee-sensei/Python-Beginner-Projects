# Display's welcome message
# ask for password
# Ask/'s what user wants to do
# check the correctness of the password
# define AgeCalculator function
# Calculator function

trial = 3
print("Oka-eri Sama!")

#loop for number of trials
for attempts in range(trial):
    password = input("Please enter secret password: ")

    #check if password match
    if password == '1234':
        print("Yo Tomodachi! What would you like to do?")
        break
    else:
        trial -= 1

        #check for more attempts
        if trial > 0:
            print("You have entered a wrong password, you have", trial, "attempts left")
        else:
            print("Limits exceeded, Refer to mail for password recovery options")
            break