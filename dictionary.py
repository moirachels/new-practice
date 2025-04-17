# ----------- Access Dictionary Items -----------
print("\n-----------ACCESS DICTIONARY ITEMS-----------")
person = {
    "name": "Moira",
    "age": 20,
    "gender": "female"
}
print(person["name"])  # Using key access
print(person.get("age"))  # Using get() method

# ----------- Change Dictionary Items -----------
print("\n-----------CHANGE DICTIONARY ITEMS-----------")
person["age"] = 21
print("Updated Age:", person["age"])

# ----------- Add Dictionary Items -----------
print("\n-----------ADD DICTIONARY ITEMS-----------")
person["hobby"] = "Painting"
print("Added Hobby:", person["hobby"])

# ----------- Remove Dictionary Items -----------
print("\n-----------REMOVE DICTIONARY ITEMS-----------")
person.pop("gender")  # Removes key 'gender'
print("After Removing 'gender':", person)

# ----------- Loop Dictionary Items -----------
print("\n-----------LOOP DICTIONARY ITEMS-----------")
for key, value in person.items():
    print(key + ":", value)

# ----------- Copy Dictionary Items -----------
print("\n-----------COPY DICTIONARY ITEMS-----------")
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# ----------- Nested Dictionaries -----------
print("\n-----------NESTED DICTIONARIES-----------")
students = {
    "student1": {
        "name": "Moira",
        "grade": 90
    },
    "student2": {
        "name": "Chelsey",
        "grade": 88
    }
}
print("Student 1 Info:", students["student1"])
print("Student 2's Grade:", students["student2"]["grade"])

# ----------- Dictionary Methods -----------
print("\n-----------DICTIONARY METHODS-----------")
print("Keys:", person.keys())  # Returns all keys
print("Values:", person.values())  # Returns all values
print("Items:", person.items())  # Returns all key-value pairs
print("Is 'hobby' in dictionary?", "hobby" in person)  # Check if key exists