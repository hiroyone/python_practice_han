print("Hello World!")

apple = "apple"

if 2 == 2:
   print("True")
else:
   print("False")

if 5 > 2:
    print("Five is greater than two!")

# This is a comment


"""This is a 
multiline docstring."""
print("Hello, World!")


"""
I am writing Python code.
This is multi-line comments in the middle
"""
x = 5
if x == 5:
    print(1000)
y = "John"
print(x)
print(y)

# Variable is hensu in Japanese

# Variable declaration is not possible in Python
# dynamic typed language
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# Output
x = "awesome" #String
print("Python is " + x)

# String Concatenation
x = "Python is "
y = "awesome"
z = x + y
print(z)

# add numbers
x = 5
y = 10
print(x + y)

# String and number cannnot be joined, so number should be converted to string
x = "Python is "
y = 5
z = x + str(y)
print(z)

"""
Review
- Different Languages 
    - Frontend, Clientside
        - HTML 
        - CSS (Bootstrap)
        - JavaScript (ReactJS, VueJS ...)
    - Backend, Serverside
        - Java (Enterprise)
        - C Family (Computation, Academics)
        - Python, Ruby (General Purpose, Prototype, OS, A.I. Web Scraping, Education)
        - Go Language (Compact and Fast, good for web services)
        - PhP (for web service)
    - Mobile
        - Kotlin (Android)
        - Swift (iOS)
    - Terminal (Mac), Commmand Prompt (Windows)
        - Bash (Mac)

- Install: Official or Anaconda (Distribution Package)

- Editor
    - VS code <- recommended
    - Jupyter Notebook <- Best for data science or A.I.

- Execution
    - Command Line (Execute file)
    - interactive shell (inc. Jupyter Notebook)

- Python features
    - Python 2.0 series and 3.0 series (3.0 is strongly recommended)
    - interpreted langauge (program is read each time) <-> compiled language
    - interactive language (immediate feedback for each statement => for better debugging)
    - dynamically typed language (no declaration, type can be changed in the middle) <-> Static Language (Java, C)
    - Indentation
    - Pythonic (Undestandable writing style, Zen princples) => Pythonista

- Tutorial
    - W3: https://www.w3schools.com/python/python_iterators.asp
"""

# Casting => Convert a value to a certain type  you want to specify
x = int(2) # Treat 2 as an integer
x = float(2)  # Treat 2 as an float 
x = str(2)
type(x) # Check the type of variable

# String Literals

sample = "Hello World!"
sample[0] # H
sample[1] # e
sample[2] # l
sample[3] # l
sample[4] # o
sample[5] # 
sample[6] # w
sample[7] # o
sample[8] # r
sample[9] # l
sample[10] # d
sample[11] # !

print(sample[10]) 
print(sample[0:5]) # Hello

# Strip is to remove a space in the beginning and end, useful for text processing
sample2 = " Hello World! "
print(sample2.strip())

# Len
x = "Hello World!"
print(len(x)) # Expect 12
x = [1,2,3,4,5] # List
print(len(x)) # Expect 5
print(x[0:len(x)]) # Choose all elements

# Convert to a lower/upper case
x = "Hello World!"
print(x.lower()) # Default argument is applied 
print(x.upper()) # Default argument is applied

# Replace/Split a string
print(x.replace("l", "r", 1))
print(x.split("o"))

# Raw Input
print("Enter your name:")
# x = input()
print("Hello " + x)


print(5 /2) # Answer is float
print(5//2) # Answer is integer => Floor

# Assignment Oprater
x = 2
x = x + 3 # Not cool
x += 3 # Pythonic
print(x)
# -=, *=, /=, <=
x = 2
x = x < 3
print(x)
x <= 3
print(x)

# Comparison Operators
x = 2 # X is equal to 2
print(x == 2) # Is X equal to 2?
print(x != 2) # Is X not equal to 2?

# Logical Oprators such as and, or, not
x = 2
print("x = {}".format(x)) # X = 2
print("X is equal to 2 but not equal to 3, yes? => {}".format(x ==2 or x !=3)) # Variable Substitution

# Membership Operators
x = ['a', 'b', 'c']
y = "a"
print(y in x)
print(y not in x)

# List is powerful
x = ["apple", "pinapple", "pen"]
print(x[1]) # List access as an element
print(x[1:2]) # List Slicing


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Length of list => how many elements in a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

# Add an item to a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # ["apple", "banana", "cherry", "orange"]

# Add an item to a specific element in a list
thislist.insert(1,"Orange")
print(thislist)

# Remove an item from a list
thislist.remove("banana")
print(thislist)

# Remove an item from a list by index
thislist.pop(0)
print(thislist)

# List Constructor
x = "This is it!"
thislistx = list(x)
print(thislistx)


# For other list operations, please refer to "https://www.w3schools.com/python/python_lists.asp"

# Tuple 
# Element is unchangeable
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant"
# # The values will remain the same:
# print(thistuple)

# Set
# Duplicate is ignored. Retrieve only unique values, and the order does not matter
thisset = {"apple", "apple","banana", "cherry"}
print(thisset)
thislist = ["apple", "apple", "banana", "cherry"] #duplicate is allowed
print(thislist)

# One application with set constructor
unique_this = set(thislist) # This will drop all duplicate
print(unique_this)
# Ref: https: // www.w3schools.com/python/python_sets.asp

x = "Hello World! My name is Han!"
x_set = set(x)
print(x_set) # Drop the duplicates

# Create a list of string, where there is no duplicate, but order does matter 
x_unique = []
for char in x:
    if char not in x_unique:
        x_unique.append(char)
print(x_unique)        

# Dictionary, a (unordered) list of key and value <= used frequently
name_dict = {"Misaki":"Tanaka", "Taro":"Yamada"}
print(name_dict)

# Access
print(name_dict["Taro"])  # Returns Yamada, equivalent to name_dict.get["Taro"]

# Change value
name_dict["Misaki"] = "Yamaguchi"
print(name_dict)

for key in name_dict:
  print(key) # print key
  print(name_dict[key]) # print value

for value in name_dict.values():
    print(value)

print(name_dict.keys()) # Print keys
print(name_dict.values()) #Print values

# Add item
name_dict["Jin"] = "Low"
print(name_dict)

print(name_dict.values())


# # For loop +> popular in Python
# item_song = '' # Empty String
# for item in x:
#     item_song += item + ' '
# print(item_song)

# # For loop for number
# x = 10
# for num in range(x): # range(0,x,1) by default
#     print(num)

# for num in range(2,x):
#     print(num)

# for num in range(0,x,2):
#     print(num)

# # For loop for string
# x = "Hello World!"
# for letter in x:  # range(0,x,1) by default
#     print(letter)


# # But! If you want to use an index number as a for-element, then use range(len(x))
# x = "Hello World!"
# for index in range(len(x)):
#     print(x[index-1]) # print "!Hello World"
# # x[-1] = x[len(x)]    


# # For loop for dictionary
# name_dict = {"Misaki": "Tanaka", "Taro": "Yamada"}
# for key in name_dict:
#     print(key)

