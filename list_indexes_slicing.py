# Do all of this in a .py file 
# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
var = [[0, 2], [4, 6], [8, 10], [12, 14]]

# Access the first list from the list of lists in step 1 by index then print it.
print(var[1])

# Access the 14 from the list in step 1 then print it.
print(var[-1][1])

# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
sub_var = ["chair", "table", "desk", "lamp", "bed"]

# Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(sub_var[-5])

# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
print("most people own at least " + str(var[0][1]) + " "+ sub_var[-5] + "s")

# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
var_two = [0.98, 8.76, 6.54, 4.32]

# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
print(var_two[1:])

# Print the slice [8.76, 6.54] from the variable you created in step 7.
print(var_two[1:3])

# Print the slice [0.98, 8.76] from the variable you created in step 7.
print(var_two[:2])
