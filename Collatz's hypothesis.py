# c0 takes user input of n number
# checks if it's even and divides it by 2
# else if odd number, 3 * c0 + 1
# loop over as long as c0 != 1
# print out the previous iterations of c0

c0 = int(input("Enter number: "))
while c0 != 1:
    print(c0)
    if c0 % 2 != 0:
        c0 = 3 * c0 + 1
    else:
        c0 //= 2
print(c0)