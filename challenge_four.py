# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.
# In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400. The first variable represents the number of gallons of gas that the car's fuel tank holds. The second variable represents the miles that the car can travel on a full tank before needing a refuel.
# Using the formula miles per gallon (MPG) = miles driven/gallons used, 
# calculate the car's MPG and display it in the output using print().  
# Use floor division instead of regular division for this calculation to get an integer instead of a float.  
# This will give a realistic approximation of miles per gallon even though floats such as 19.8 round down a large amount 
# when using floor division since sometimes, car manufacturers sometimes exaggerate miles per gallon.  
# In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank and miles it can travel on a full tank with two different print statements.


from random import *

fuel = randint(50,200)
miles = randint(400,1000)


print("The car can travel " + str(miles // fuel) + " miles per gallon.")
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")
