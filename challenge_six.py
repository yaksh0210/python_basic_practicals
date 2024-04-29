# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.
# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.
# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.


from random import randint

func = randint(1,10)

if func == 1:
    print("the roman number for generated number "+ str(func) + " is I.")
if func == 2:
    print("the roman number for generated number "+ str(func) + " is II.")
if func == 3:
    print("the roman number for generated number "+ str(func) + " is III.")
if func == 4:
    print("the roman number for generated number "+ str(func) + " is IV.")
if func == 5:
    print("the roman number for generated number "+ str(func) + " is V.")
if func == 6:
    print("the roman number for generated number "+ str(func) + " is VI.")
if func == 7:
    print("the roman number for generated number "+ str(func) + " is VII.")
if func == 8:
    print("the roman number for generated number "+ str(func) + " is VIII.")
if func == 9:
    print("the roman number for generated number "+ str(func) + " is IX.")
if func == 10:
    print("the roman number for generated number "+ str(func) + " is X.")
