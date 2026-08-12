#Strings, Integers, Float, and Boolean

#Strings
first_name = "Lestat Marius"
middle_name = "Benoza"
last_name = "Laguna"
food = "Adobong Baboy"
email = "kiandiverson@gmail.com"

print(f"Hello {first_name} {middle_name} {last_name}!")
print(f" I love {food}")
print(f" My email address is {email}")

#Integers
age = 18
favorite_number = 67
group_of_friends = 10

print(f" I am {age} years old.")
print(f" My favorite number is {favorite_number}.")
print(f" I have {group_of_friends} friends in my group.")

#Float
price = 6.7
grades = 89.5
distance = 3.5

print(f" The price of the item is Pesos{price}.")
print(f" My grades is: {grades}.")
print(f" The distance from my house to school is {distance}km.")

#boolean
is_student = True
for_sale = False
is_online = True
is_parent = True

if is_student:
    print("I am a student.")
else:
    print("I am NOT a student.")

if for_sale:
    print("The item is for sale.")
else:
    print("The item is NOT for sale.")

if is_online:
    print("I am currently online.")
else:
    print("I am NOT currently online.")

if is_parent:
    print("I am a Parent")
else:
    print("I am NOT a parent")

#Typecasting = The process of converting one data type to another str(), int(), float(), bool()
name = "Lestat Marius"
age = 18
height = 5.7
is_student = True

age = float(age)

print(age)

#input() = A function that prompts the user to ender data Returns the entered as a string

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}!")
print(f"You are {age} years old.")