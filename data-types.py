# Variables :-
# Variables are a type of container which is used to store values.

year = 2026
name = 'Utkarsh'
work = 'Learning python :>'
male = True

print('My Name : ', name)
print('What are you doing ? ', work)

# Data Types :-
# Primarily, it means differnet format of data types like letters, numbers, etc.

age = 16  # integer
height = 175.5  # float
school = 'Sankat Mochan Public School'  # strings
is_student = True  # boolean
bad_habits = None  # none

print("What is his age ? ", age)

# Operates :-
# Used to perform actions in python.

# 1. Arithmetic Operator : + - * / etc.
a = 99
b = 23 - a / 3
print(a + b)

# 2. Assignmetn Operator : = += -= etc.
b += a + b
print(b)

# 3. Comparison Operator : == >= <= > < != etc.
c = b <= a
print(c)

# 4. Logical Operator : and, or, not.
c = False or True
print(c)

# Truth Table of or :-
print('\nTrue or False is ', True or False)
print('True or True is ', True or True)
print('False or True is ', False or True)
print('False or False is ', False or False)
print('\nIt\'s VICE VERSA is the same.')

# # Truth Table of and :-
print('\nTrue and False is ', True and False)
print('True and True is ', True and True)
print('False and True is ', False and True)
print('False and False is ', False and False)
print('\nIt\'s VICE VERSA is the same.')

# not functions :-
# Makes the boolean values change means if
not(True) == False
not(False) == True

# type() function :-
# It is used to find the data type of given value or variable in python.

print(type(a))
print(type(b))

# Type-Casting :-
# Typecasting in coding means to change the data type of given value or variable.
 
print(str(54))
print(float(10))
print(int(90.4))
