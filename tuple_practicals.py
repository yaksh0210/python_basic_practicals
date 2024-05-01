# creating a tuples

tuple_one = ("a", "b", "c")
tuple_two = (1, 2, 3)
tuple_three = (1 ,True , "A")
print(tuple_one)
print(tuple_two)
print(tuple_three)

#slicing of tuple

tuple_four = (1 ,2, 3, 4, 5, 6)

print(tuple_four[1:])
print(tuple_four[2:4])
print(tuple_four[:5:2])

#index in tuple

tuple_five = ("a", "b", "c", "d", "e")
print(tuple_five[2])

#tuple looping

#for loop 

city = ("ahmedabad", "rajkot", "vadodra", "vapi", "surat")

for c in city:
    print(c)


#while loop 

count = 0
while count < len(city):
    print(city[count])
    count += 1


#tuple methods

# .count() method

tuple_six = (1, 1, 2, 3, 4, 5, 5, 6, 5, 6, 5)
print(tuple_six.count(1))
print(tuple_six.count(5))

# .index() method

tuple_seven = (2, 3, 8, 12, 15)
print(tuple_seven.index(12))