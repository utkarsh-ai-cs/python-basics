# Lists :-
# Lists are containers to store a set of values of any data type.
# Lists are ordered and changeable (mutable).

# Syntax : 
Cars = ['BMW', 'Mercedes', 'Audi', 'Honda']
no_ofCars = [2, 5, 2, 4]

# Accessing List Items :-
# Eg : 

names =        ['Utkarsh', 'Ansh', 'Palak', 'Yashdeep', 'Kartik', 'Vaibhav'] #->  Utkarsh  Ansh  Palak  Yashdeep  Karitk  Vaibhav
# Index :          0         1        2         3          4          5      ->     0       1     2       3         4        5  
# Reverse Index : -6        -5       -4        -3         -2         -1      ->    -6      -5    -4     -3         -2      -1 { The values are in Negative. }

print(names[2])
print(names[-3])

# List Slicing :-
# getting / slicing a specific part of the List in python.
print(names[1:3])   # Output -> [1, 2, 3]

# Changing List Elements :-
names[2] = 'Isha'


# List Functions / Methods :-

# append(value) :- Adds value at end of the list.
names.append('Devansh')

# insert(index, value) :- Adds value at the given index.
names.insert(1, 'tanya')

# remove(value) :- Removes the first occurence of value.
names.remove('tanya')

# pop() :- Removes the last element.
names.pop()

# count(value) :- Counts how many times value appears.
names.count('Ansh')

# sort() :- Sorts the values in the list (ascending).
names.sort()

# reverse() :- Reverses the list.
names.reverse()

# len() :- Returns the size of the list.
print(len(names))

# Loops with Lists :-
for item in fruits:
    print(item)

# Nested Lists :-
nested = [ [1,2], [3,4], [5,6] ]
print(nested[1])        # Output -> [3,4]
print(nested[1][0])     # Output -> 3


# Tuples :-
# Tuples are similar to Lists but they are *immutable* (cannot change).
# Tuples use parentheses () not square brackets [].

# Syntax :-
# my_tuple = (value1, value2, value3)
colors = ('Red', 'Green', 'Blue')

# Accessing Tuple Items :-
# Same as LIST :)
print(colors[1])       # Output -> Green
print(colors[-1])      # Output -> Blue

# Tuple is immutable :- you cannot do
# colors[1] = 'Yellow'   # This will give an error

# Tuple Functions :-

# count(value) :- Counts how many times value in tuple.
print(colors.count('Red'))

# index(value) :- Finds the first index of value.
print(colors.index('Blue'))

# Why use Tuple ?
# - Faster than list
# - When values should not change

# List vs Tuple :-
# 1) List uses [] & is changeable.
# 2) Tuple uses () & is not changeable.
# 3) You can add/remove items in list, not in tuple.
# 4) Tuple is slightly faster than list.
