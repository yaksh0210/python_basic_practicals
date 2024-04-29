# Do all of this in a single.py file

# Create a variable and assign it the string "Just do it!"
ex = "Just do it!"

# Access the "!" from the variable by index and print() it
print(ex[10])

# Print the slice "do" from the variable
print(ex[5:7])

# Get and print the slice "it!" from the variable
print(ex[8:])
# Print the slice "Just" from the variable
print(ex[:5])
# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
print("don't " + ex[5:] )

