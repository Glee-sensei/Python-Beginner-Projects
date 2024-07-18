my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
# Write your code here.
for member in my_list:
    # check for presence and add to unique_list if not found
    if member not in unique_list:
       unique_list.append(member)


print("The list with unique elements only:", unique_list)
print(my_list)