# creating a set 

myset = {"apple", "orange", "banana", 1 , False}
print(myset)

# len() in set

print(len(myset))

# set() function

tup = set(("apple","banana","banana"))
print(tup)

# Add() to add item in set

myset.add("coffee")
print(myset)

# update() to add item from another set

tup.update(myset)
print(tup)

# in and not in

print ("cherry" in myset)
print ("apple" not in tup)

# .remove() and .discard() methods

myset.remove("banana")
print(myset)

tup.discard("coffee")
print(tup)

# .pop()

tup.pop()
print(tup)

# joins in set

set1 = {1, 2, 3, "a", "c"}
set2 = {"a", "b", "c", 1}

set3 = set1.union(set2)
print(set3)

set4= set1.intersection(set2)
print(set4)

set5 = set1.union(set2,set3)
print(set5)

set6 = set1.difference(set2)
print(set6)