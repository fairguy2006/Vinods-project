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
print("After adding a new key-value pair, the dictionary is:")
for key, value in person.items():
     print(key + ":", value)
#Update a Value in the Dictionary
person['age'] = 31
print("updated age:" , person["age"])
person["address"] = { "city": "New Delhi", "Zip": "560084" }
for key, value in person.items():
    if isinstance(value, dict):
        for subkey, subvalue in value.items():
            print(subkey.capitalize() + ":", subvalue)
    else:
        print(key.capitalize() + ":", value)
    # User's Favourite book and movie
favorites = {}
favorites["book"] = input ("what is your favourite book? ") # type: ignore
favorites['movie'] = input("what is your favourite movie? ")
print("Your favorites:")
for key, value in favorites.items():
    print(key.capitalize() + ":", value)
