
## Tuples

# Tuple is a built-in data type in Python used to store collections of data.
# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.

print("\n-----------FIRST TUPLE EXAMPLE-----------")
moira_chelsey = (21, "female", "SBIT-2I", 1.25)
print(moira_chelsey)

## MAIN TUPLE EXAMPLE
print("\n-----------MAIN TUPLE-----------")
grocery_list = ("Cocoa Powder", "Honey", "Wheat Bread", "Tortilla Wrapers")
print(grocery_list)


# UPDATING TUPLES
# To update a tuple, you can convert the tuple into a list, change the list, and convert the list back into a tuple.
print("\n-----------UPDATED TUPLE-----------")
updated_list = list(grocery_list)
updated_list[3] = "Banana"
grocery_list = tuple(updated_list)

print(grocery_list)

## UNPACKING TUPLES
# Each value from the tuple gets unpacked into its own variable.
print("\n-----------UNPACKING TUPLES-----------")

item1, item2, item3, item4 = grocery_list
print("\nGrocery List:")
print("Item #1: " + item1)
print("Item #2: " + item2)
print("Item #3: " + item3)

# LOOPING TUPLES 
# We use for loops
print("\n-----------LOOPING TUPLES-----------")
for y in grocery_list:
    print(y)

# JOINING TUPLES
print("\n-----------JOINING TUPLES-----------")
miscellaneous = ("Earbuds", "Towels", "Phone Case")
all_groceries = grocery_list + miscellaneous

print(all_groceries)

## TUPLE METHODS
print("\n-----------TUPLE METHODS-----------")
# .index() example
honey_index = grocery_list.index("Honey")
print("Index of 'Honey':", honey_index)

# .count() example
banana_count = grocery_list.count("Banana")
print("Number of times 'Banana' appears:", banana_count)
