# Create and Print a Dictionary
person = {"name" : "Amar", "age" : 30, "city"  : "New Delhi"}
print("Here is a dictionary about a person:" )
      # Access Values in a Dictionary
print("Name:", person["name"])
print("The person's age is :", person["age"])
print("The person lives in:", person["city"])
# Add a New Key-Value Pair to the Dictionary
person["occupation"] = "Engineer"
person["hobby"] = "reading"
print("Now the dictionary is:")
print("After adding a new key-value pair, the dictionary is:")
for key, value in person.items():
     print(key + ":", value)
#Update a Value in the Dictionary
person['age'] = 31
print("updated age:" , person["age"])

