"""
Dictionaries
"""

user_dictionary = {"username": "dzzzz", "name": "dzak", "age": "100"}

user_dictionary["married"] = False
print(user_dictionary.get("username"))
print(len(user_dictionary))

for k in user_dictionary:
    print(k)

for k, v in user_dictionary.items():
    print(k, v)

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

del user_dictionary

user_dictionary = {"username": "dzzzz", "name": "dzak", "age": "100"}

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary)  # the age in dictionary 1 wouldn't pop

user_dictionary2 = user_dictionary
user_dictionary2.pop("age")
print(user_dictionary)  # the age in dictionary 1 would pop too
