# Strings :-
# String is a data type, basically a sequence of alphanumeric characters enclosed within quotes.

name = 'Utkarsh' # Way-1 : single quotes ''
School = "Sankat Mochan Public School" # Way-2 : double quotes ""
Poem = '''
Twinkle Twinkle Little Star,
How I wonder what you are,
Up above the sky so high,
Like a diamond in the Sky.
''' # Way-3 : tripe quotes ''' '''
    # also for multiple lines


# String Slicing :-
# String Slicing means getting / slicing a specific part of the strings in python.

# Slicing is done using the INDEXES of the strings :-
# Eg :  name = ' Utkarsh '  ->  U  t  k  a  r  s  h
# Index :        0123456    ->  0  1  2  3  4  5  6
# Reverse Index :7654321    -> -7 -6 -5 -4 -3 -2 -1 { The values are in Negative. }

# Syntax :  variable[ ind_start : ind_end + 1 ]

name = 'Devansh'
print(name[3:7])


# Slicing with Skiping Value :-
print(name[0:7:2])  # The Third value is the escape sequence [ Default is 1 and with 2 : one letter would be escaped ]


# STRINGS FUNCTIONS :-

city = 'Mumbai, Kolkata'

# Length Function [ .__len__() ] :-
# This function returns the length of the string.
print(city.__len__())

# Endswith Funtion [ .endswith(value) ] :-
# This function tells whether the variable ends with the entered value or not & answers in boolean values.
print(city.endswith('wow'))

# Count Function [ .count(value) ] :-
# This funtion counts the number of occurences of value, presented in the string.
print(city.count('m'))    # here ' m ' & ' M ' will be counted differently.

# Capitalize [ .capitalize() ] :-
# This function capitalize the first letter of the string.
print(city.capitalize())

# Find function [ .find(value) ] :-
# This function finds a word or letter and returns it's first occurence index in the word.
print(city.find('bai'))

# Replace Function [ .replace(old, new) ] :-
# This function replaces the old word / letter with the new given word / letter within the string.
print(city.replace('Kolkata', 'Chennai'))


# Escape Sequence Characters :-
# \n  -  new line
# \t  -  tab
# \'  -  single quotes
# \\  -  back slash