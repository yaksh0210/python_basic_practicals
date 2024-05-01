#use of del method in list
list_one = ["hello" , "hey", "bonjour", "namaste"]
del list_one[1]
print(list_one)

#use of .remove() method in list 
list_one.remove("hello")
print(list_one)

#use of .append() method in list
list_one.append("chin-han")
print(list_one)

#use of .insert() method in list
list_one.insert(0,"master")
print(list_one)

#use of .sort() method in list

list_one.sort()
print(list_one)

list_one.sort(reverse=True)
print(list_one)


#use of .index() method in list
print(list_one.index("namaste"))

#user of .pop() method in list
gen_list = list_one.pop(2)
print(list_one)