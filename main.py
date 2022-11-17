import math
import keyword
import time
import operator
import array as arr

# print("hello world!")
# print(" Created by Guido van Rossum in 1991")
# ------------
"""
a = 3
b = 4
c = "Python"
print(a + b)
print(c)
print("List-It is mutable data structure")
nums = []
nums.append(29)
# nums.append(08)
nums.append("String")
print(nums)
"""

"""
Multi line comment
"""

"""
num = int(input("Enter any number - "))
age = int(input("Enter yor age - "))
#print("Welcome", name)
print("Age after ",num," years :",num+age)
"""

"""
print("Selection in Python is made using the two keywords ‘if’ and ‘elif’ and else (elseif)")
num = float(input("Enter any number - "))
if(num>0):
    print("Positive Number")
elif(num<0):
    print("Negative Number")
else:
    print("Zero")
"""

"""
print("Functions are defined by def name (arguments):")
print("Example-")

a = 14

def greet():
    print("Function started")
    print("Here a is ",a)
    print("Function ended")


def call():
    print("Outside function")
    greet()

call()
a = 12
print("Here a is ",a)

for count in range(1,6):
    print(count.__add__(count))
"""

# print(keyword.kwlist)

"""
print(False==0)
print(True==1)
print(True+True+True)
print(False-True+True-True)
print(None==0)
print(None==[])
"""

"""
print(True or False)
print(True and False)
print(not True)
if('a' in 'Dhairya'):
    print('Dhairya')
else:
    print('Saraswat')
print("\r") #For line break
for i in 'Dhairya Saraswat':
    print(i,end=" ")
print('\r')
print('' == '')
print({} is {})
"""

"""
for i in range(10):
    if i==6:
        continue
    else:
        print(i, end=" ")
print("Loop ended")
"""
"""
a = 5
print("The value of a is ",str(a))
print(a if 20>100 else 0)

def fx():
    print("Inside a function - ")

    def inner_fx():
        b = 15
        print(b)

    inner_fx()
    print(a)
    # print(b) out of scope


fx()
j = 1
while (j <= 5):
    print(j, end=" ")
    j = j + 1
"""

""" Taking input from the user and showing output 
#name = input("Enter your name - \n")
#age = int(input("Enter your age - \n "))
#alary = int(input("Enter your salary - \n "))
name,age,salary = input("Enter your details - \n").split()
print("Name is {} , age is {} and salary is {}".format(name,age,salary))
print(name)
print(age)
print(type(name))
print(type(age))
print("") #prints an empty line and \n-for new line
print(salary+age)
"""

"""
date = 29
month = "August"
year = 2001
print(date,month,year,sep="-")
seconds = 3
for i in reversed(range(seconds+1)):
    if i>0:
        print(i, end="\n")
        time.sleep(1)
    else:
        print('Happy Birthday')
print("", end="@")
print("Dhairya ", sep="", end="")
print("Saraswat")
print("Bye".center(40, "*")) # ljust and rjust
"""

"""
# Identity Operator (is and is not) -Check if two values are located on the same part of the memory
a = 10
b = 20
c = a
list = [10, 15]
print(a is b)
print(a is c)
print(a is not c)

# Membership operator (in and not in) - Used to test whether a value or variable is in a sequence
print(a in list)
print(b in list)

print(5 / 5)  # float division
print(5 // 5)  # Integer division  //-Floor division
print(a if a < b else b)  # Ternary Operator

print("22" * 4)  # Prints 22 four times
print(2 * 4)  # 8
print(any([True, True]))
print(any([]))
print(any([False, False]))
print(any([False, True]))
print(all([True, True]))
print(all([]))
print(all([False, False]))
"""

"""
a = 54
b = 45
c = "Dhairya "
d = "Saraswat"
print(operator.add(a, b))
print(operator.sub(a, b))
print(operator.mul(a, b))
print(operator.truediv(a, b))  # divide
print(operator.floordiv(a, b))  # floordiv
print(operator.pow(a, b))
print(operator.mod(a, b))
print(operator.eq(a, b))  # equal
print(operator.gt(a, b))  # greater than
print(operator.ge(a, b))  # greater than or equal to
print(operator.ne(a, b))  # not equal to
print(operator.concat(c, d))
print(operator.contains(c, d))
print(operator.invert(a))
"""

# Data types
""" 
Data types 
1. Strings
A string is a sequence of characters that can be a combination of 
letters, numbers, and special characters. It can be declared in python by using single quotes,
 double quotes, or even triple quotes.
2. Lists
They are just like the arrays declared in other languages. But the most powerful thing is that 
list need not be always homogeneous. A single list can contain strings, integers, as well as other objects.
l = [ -,-,-]
3. Tuples
A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception that tuples 
cannot be changed once declared.
t = ( -,-,-)
4. Iterations
 Iterations or looping can be performed in python by ‘for’ and ‘while’ loops. Apart from iterating upon a particular 
 condition, we can also iterate on strings, lists, and tuples.
"""

# Strings
"""
n = '''
      First Line
      Second Line
      Third Line
    '''
# print(n)

a = "Dhairya"
b ="{}{}{}".format('M', 'A', 'N')
print(b)
b ="{2}{0}{1}".format('M', 'A', 'N')
print(b)
c ="{first}{second}{third}".format(first="Coding",second="is",third="fun")
print(c)
print(a[-1])
print(" Initial String", a)
# Deleting a string del(a)
print("Deleting a character ", a[0:2]+a[3:])
print("Reverse string", a[::-1])   # Reverse
print("Another Reverse by join ", "".join(reversed(a)))
a = "Saraswat"
print("Updated String", a)
# To access a range of characters in the String, the method of slicing is used.
# Slicing in a String is done by using a Slicing operator (colon).
print("Slicing", a[3:6])
print("Slicing", a[3:-2])
"""

# Lists
"""
L = [1, "Dhairya", 8*2]  # List
print("List", L)
L.append("S")
print("List", L)
L.pop()
print("List", L)
print("List Index position 1 ", L[1])  # Index starts from 0
ML = [['A', 'B'], ['C']]
print("Multi-dimensional Lists", ML)
print("Multi-dimensional List at index 0 1 - ", ML[0][1])
print("Length -", len(L))
print("Negative Indexing starts from last ", L[-1])
M = ['Rizor', 'Bloodstorm']
L.append(M)
print("Adding second list ", L)
# For adding elements at the desired position , insert method  is used
L.insert(2, "Saraswat")
print("Adding element at the specific position ", L)
# For adding multiple elements at the end , extend method is used
L.extend(['Ariza', "Bloodstorm"])
print("Adding multiple element at the same time ", L)
L.reverse()
print("Reversing a list", L)
# Remove- Remove() method only removes one element at a time, to remove a range of elements
L.remove('Bloodstorm')
print("Removing a element ", L)
L.pop()
print("Pop removes last element ", L)
"""

# Tuples
"""
a = "Dhairya"
t = (1, "D", 8-9)    # Tuples
u = (2, "S", 9*3+2)  # *3 Value will be printed three times
v = (t, u)
print("Concatenation of two tuples ", t+u)
print("Tuple formed by combining two tuples ", v)
print("Tuples", t)
print("Tuple at index 1 ", t[1])
# t.append("S")  Cannot append or delete in tuples
# print("Tuples", t)
i = 1
print("Iteration in loop")
while i <= 10:
    print(i, end=" ", sep="\n")
    i += 1

for j in a:
    print(j, end=" ")
print()
print("Iteration in range")
for k in range(5, 10):
    print(k, end=" ")
Tuple1 = tuple('DHAIRYASARASWAT')
print()
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

# deleting a tuple del Tuple1
"""

# Set
"""
# A Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
# there is no index in set
a = set(["Dhairya", "Dhairya", "Saraswat"])
num = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(num)
# add - adding element at the end , only one at at time
num.add(10)
print(num)
# update - adding multiple element at a time
num.update([0, 11])
print(num)
print("12" in num)
# remove & discard - For removing elements
# num.remove(11)
num.discard(11)
print(num)
# Pop only removes first element from the set
num.pop()
print("Pop -", num)
# num.clear()
# print("Clear set -", num)
"""

# Dictionary
"""
# Dictionary in Python is a collection of keys values, used to store data values like a map.
# Dictionary holds key:value pair.
# Here keys are immutable and can't be repeated while values can be of any data type and can be duplicated.
Dict = {1: "Dhairya", 2: "Saraswat"}
print(Dict)
# Nested Dictionary
Data = {1: "Python data types", 2: "includes", 3: {'A': 'String', 'B': 'Lists', 'C': 'Tuples', 'D': 'Sets',
                                                   'E': 'Dictionary', 'F': 'Arrays'}}
print(Data)
Data[2] = '-'
print(Data)
Data[4] = "-"
print(Data)
# Accessing element by index
print("Data at index 3 ", Data[3])
print("2 method by getting data at index 3 ", Data.get(3))
print("Accessing an element in nested dictionary - ", Data[3]['E'])
Copy = Data.copy()
print("Copy of a dictionary - ", Copy)
Copy.clear()  # Clear all the elements from the dictionary
print("Empty dictionary after clear ", Copy)
print("Dictionary items - ", Data.items())  # Returns a list containing a tuple for each key value pair
print("Dictionary keys - ", Data.keys())  # Returns a list containing dictionary’s keys
Data.pop(4)  # Pop element removes the element with the specified key
print("After popping out 4 - ", Data)
Data.popitem()  # popitem removes last element from dictionary
print("Pop item removes last element ", Data)
Data.update({3: {'A': 'String', 'B': 'Lists', 'C': 'Tuples', 'D': 'Sets', 'E': 'Dictionary', 'F': 'Arrays'}})
print("Adding new element - ", Data)  # Adding new element by update
print("Getting values - ", Data.values())  # Getting values
"""
"""
# Arrays

# An array is a collection of items stored at contiguous memory locations having same data type.
# import array module - import array as arr
a = arr.array('i', [1, 3, 4])  # Creating array
print(a)
i = 0
while i < 3:
    print(a[i], end=" ")
    i += 1

# inserting value in array .insert(index, value)
# By insert or by append (adds element into the end)
print("\nAdding elements into an array - ")
a.insert(1, 2)
a.append(5)
for i in a:
    print(i, end=" ")
    i += 1
# Accessing element from the array -
print("\nAccessing element at index 2 - ", a[2])
# Removing element from the array -
# By default pop will delete last element from an array so we can pass index
a.pop(2)
print("Removing element by pop - ", a)
a.remove(4)
# Remove deletes 1 occurrence of an element
print("Removing element by delete - ", a)
b = a[:]
print("Printing all elements in slicing - ", b)
b = a[1:]  # a[start:range]
print("Printing all elements in slicing taking from position 1 - ", b)
# Searching element in an array - by .index(1)
#  index() method. This function returns the index of the first occurrence of value mentioned in arguments.
print("Finding index position of 5 -", a.index(5))
# Updating elements in an array
a[2] = 6
print("After updating index at position 2 -", a[2])
"""

"""
# Identity operator - is and is not
a = 23
b = 26
print(a is b)
print(a is not b)

# Membership Operator - in and not in
l = [20, 21, 22, 23, 24, 25]
if a in l:
    print(a, "is present in list")
else:
    print(a, "is not present in list")
if b not in l:
    print(b, "is not present in list")
else:
    print(b, "is present in list")
"""

# Control Flow
# Decision-making statements in python decide the direction of the flow of program execution.
# If else
# It is used to decide whether a certain statement or block of statements will be executed or not
# i.e if a certain condition is true then a block of statement is executed otherwise else block.

"""
a = 10
if a % 2 == 0:
    print("Even")
    print("If Block")
    if a < 15:
        print(a, "is smaller than 15")
    if a > 5:
        print(a, "is greater than 5")
else:
    print("Odd")
    print("Else Block")
# if-else ladder
c = float(input("Enter any number : "))
if c > 0:
    print("Positive")
elif c < 0:
    print("Negative")
elif c == 0:
    print("Zero")
"""

"""
# Chaining operations in python
a = 5
print(a < 10 < 20)
print(a*2 == 1*10)
print(10 > a < a-1)
b, c, d = 7, 6, 5
print(a == d < c < b)
print(a is d)
print(a is b)
"""

"""
# For loop - sequential traversal
# Syntax - for var in iterable:
#           statements
lists = ['Dhairya', 'Saraswat']
for i in lists:  # Using loop in lists
    print(i, end=" ")
print("")
d = {'1': 'Dhairya', '2': 'Saraswat'}
for i in d:  # Using loop in dictionary
    print(i, d[i])
a = "DHAIRYA SARASWAT"
for i in a:  # Using loop in strings
    print(i, end=" ")
print(" ")

# Loop control statements
# Python continue Statement returns the control to the beginning of the loop.
for i in a:
    if i == 'A':
        continue
    print(i, end=" ")
print(" ")

# Python break statement brings control out of the loop.
for i in a:
    if i == 'S':
        break
    print(i, end=" ")
print(" ")

# The pass statement to write empty loops. Pass is also used for empty control statements, functions, and classes.
for i in a:
    pass
    print(i, end=" ")
print(" ")

# Python range() is a built-in function that is used when a user needs to perform an action a specific number of times.
# range(start, till num)  -- end is not shown in result
for i in range(10):
    print(i, end=" ")
print(" ")
total = 0
for i in range(1, 10):
    total = total + i
    print(i, end=" ")
print("\rSum of first 10 numbers is", total)
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop ended 5 will not be printed")
"""

# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# And when the condition becomes false, the line immediately after the loop in the program is executed.
# Syntax -
# while expression:
#       statements
"""
name = "Dhairya"
i = 0
a = int(input("Enter any number "))
while i < a:
    print(name)
    i += 1
b = [1, 2, 3, 4, 5]  # list
while b:
    print(b.pop())
print("\rAll elements are popped out")
total = 0
while a != 0:
    a = int(input('Enter a number (0 to quit): '))
    total = total + a
print("Numbers you entered gives sum", total)
"""

# Different looping techniques -
"""
# 1. Enumerate - enumerate() is used to loop through the containers printing the index number
# along with the value present in that particular index.
for key, value in enumerate(['A', 'B', 'C', 'D']):
    print(key, value)

# 2. Zip -zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially.
ques = ['Name -', 'Age -']
ans = ['Dhairya', '21']
for quest, answer in zip(ques, ans):
    print(quest, answer)

# 3. Sorted
lis = [1, 2, 3, 4, 5, 5, 1, 3]
lis1 = ['A', 'Z', 'B', 'Y', 'b', 'a', 'z', 'S']
print("Sorted list - ", sorted(lis))
print("Sorted list1 - ", sorted(lis1))
print("Sorted list without duplicate- ", sorted(set(lis)))

# 4. Reversed
print("Reverse list -")
for j in reversed(lis):
    print(j, end=" ")
print("\nReverse list1 -")
for i in reversed(lis1):
    print(i, end=" ")

# 5. Items
print("")
lis2 = {"Language": "Python", "Topic": "Loops"}
for i, j in lis2.items():
    print(i, j)
"""

# Functions
"""
# It is a block of statements that returns the specific task.
# Syntax - def function_name(parameter):
#              statements
#             return expression
def fun():
    print("Function created")
print("Calling function")
fun()
print("Function called")

def add(num1: int, num2: int) -> int :
    num3 = num1 + num2
    return num3
print("Add-", add(15, 14))

n = 18
def checkprime(n):
    if n > 1:
      for i in range(2, n):
          if (n % i) == 0:
           print(n, "is not a prime number")
           print(i, "times", n // i, "is", n)
           break
          else:
           print(n, "is a prime number")
    else:
      print(n, "is not a prime number")


print(checkprime(n))

# Default arguments
def myfun(x, y=50):
    print(x)
    print(y)
myfun(30)
# Keyword arguments
def profile(fname, lname):
    print(fname, lname)
profile(fname="Dhairya", lname="Saraswat")
# Docstring - The first string after the function is called the Document string
# Syntax: print(function_name.__doc__)
x = int(input("Enter any number :"))
def ed(x):  
    if(x%2==0):
        print("Even")
    else:
        print("Odd")
print(ed.__doc__)  
print(ed(x))
# return statement
def sq(y):
    return y**2
print(sq(3))
"""
# Pass by reference can change the value. Ex-
def myfx(x):
    x[0]=20
list3 = [10, 30]
print("Value before", list3)
myfx(list3)
print("Value after", list3)
# Pass by value cannot change original value. Ex-
def myfx1(x):
    x = 20
list4 = 10
print("Value before", list4)
# myfx(list4)   # Error- 'int' object does not support item assignment
print("Value after", list4)
# Anonymous functions - Functions without a name
# lambda keyword is used to create anonymous functions.
def cube(x):
    return x * x * x
cube1 = lambda y: y * y * y
print(cube(10))
print(cube1(10))
# Nested Functions
def f1():
    greet = "Welcome"
    def f2():
        print(greet)
    f2()
f1()

# Generator-Function- It generates a value with yield keyword rather than return
i = 1
def Genfx(i):
    yield i
    i += 1
    yield i
    i += 2
    yield i
for value in Genfx(i):
    print(value)
""