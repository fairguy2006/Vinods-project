# Create and Print a List 
fruits =["apple" , "banana" , "orange" , "kiwi" , "mango"]
# Print the list
print("Here is a list of fruits:", fruits)
# Added a new fruit
fruits.append("grape")
# Printed the updated list
print("Now the list is:", fruits)
# Looped through the list and printed each fruit
print("let's print each fruit:")
for fruit in fruits:
    print(fruit)
#  List Slicing
    fruits = ["apple" , "banana", "orange", "kiwi", "mango","grape"]    
#get the first three fruits
first_three = fruits[0:3]
print("the first three fruits are:", first_three)
# get the last two fruits
last_two = fruits[-2:]
print("The last two fruits are:", last_two)
#  Find the Length of a List
print("there are", len(fruits), "fruits in list")
# Remove "banana" from the list
fruits.remove("banana")
print("after remoiving banana:" , fruits)
# Check if "kiwi" is in the list
if "kiwi" in fruits:
    print("kiwi is in the list!")
else:
    print("kiwi is not in the list!")
# Removing an Item That’s Not There
if "pear" in fruits:
    fruits.remove("pear")
else:
    print("pear is not in the list, so it cannot be removed.")






