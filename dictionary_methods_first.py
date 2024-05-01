# Do all of this in a .py file in 
# create a variable and assign it the following dictionary: {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

dic = {"Queen": "Bohemian Rhapsody", 
       "Bee Gees": "Stayin' Alive", 
       "U2": "One", 
       "Michael Jackson": "Billie Jean", 
       "The Beatles": "Hey Jude", 
       "Bob Dylan": "Like A Rolling Stone"
}



# print the length of the dictionary.

print(len(dic))

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.

for key in dic.keys():
    print(key)

# print all of the values from the dictionary using the .values() method.
for val in dic.values():
    print(val)

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key,val in dic.items():
    print(key,val)

# use the .get() method to check the dictionary for the key "Promise of the Real" and create a message that will print if the key is not found in the dictionary.
print(dic.get("Promise of the Real","That is not a key that appears in the dictionary."))


