#use of dictionary and creation with key:value pair

dic = {"hello":"namste","how are you":"kaise ho aap"}
print(dic["how are you"])
print("what can you say about " "\"" + dic["how are you"] +"\" greetings from an indian") 

#dictonaries are unordered while list always reamins in ordered

first = {0:1,1:2 ,2:3}
second = {2:3,0:1,1:2}

print(first==second)

list1 = (1,2,3)
list2 = (3,2,1)

print(list1 == list2)


#in and not in  operator
first = {0:1,1:2 ,2:3}
print(1 in first)
print (4 not in first)

#use of .key() fuction
name = {1990:"james" , 1998:"tom", 2002:"steve", 2004:"robort"}
print(name.keys())

for key in name.keys():
    print(key)

#use of .value() fuction
print(name.values())

for val in name.values():
    print(val)

#use of .items() function
print(name.items())

for item ,val in name.items():
    print(item ,val)

#convert into list data type
print(list(name.values()))

#perticular way to check values in dictionary
print("tom" in name.values())


#use of .get() method
print(name.get(2002,"2002 is not a key in name"))

#use of .fromkeys() method

ex1 = {}.fromkeys("Adc","ABC street NJ,1234")
print(ex1)

#use of .pop() method

ex2 = {"car":"mastung" , "song":"Addy nagar" , "spec":"armaani"}
print(ex2.pop("song"))
print(ex2)

#use of .popitem() method
ex2.popitem()
print(ex2)

#use of .clear() method

ex3 = {"jan":"kite","feb":"mahashiv", "mar":"holi", "apr":"exams"}
print(ex3)
ex3.clear()
print(ex3)

#use of .update() method
ex4 = {"jan":"kite","feb":"mahashiv", "mar":"holi", "apr":"exams"}
ex5 = {"may": "vacation"}
ex4.update(ex5)
print(ex4)