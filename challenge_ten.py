# Create a function which takes one positive integer as its input and returns its factorial.

# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))