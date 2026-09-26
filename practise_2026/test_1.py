# python variable cannot start with a
# 'Number', 
# whitespace in between, 
# special characters except underscore, reserved keywords 


user_name:str = 'Gagan' # type annotation
# user_name = False # it can still be assigned to other data types
# print(type(user_name))


# function with type annotation
def greet(name:str, age:int):
    if age >= 18:
        return(f'{name} is an adult with age of {age} years old')

    return(f'{name} is not an adult with age of {age} years old')

print(greet(user_name, 28))


# quick_ques = input('Tell me about yourself ? ')
# print(quick_ques)

x = 9
y = 3

result = x/y
print(result) # 3.0
# even though, x and y are integers but output is float, reason being divide operator it returns float values

result2 = x % y
print(result2) # 0
# modulo operator returns the remainder of the division

# num_input = int(input('enter a number: '))
# print('The number you entered is: ', num_input, type(num_input)) # type casting to int, as input() returns string by default

#* string methods #
name = 'Gagan'
print(name.upper()) # GAGAN

print(name.lower()) # gagan

print(name.capitalize()) # Gagan

print(name.replace('G', 'L')) # Lagan

print(name.split('a')) # ['G', 'g', 'n']

print(name.find('g')) # 2, returns the index of the first occurrence of the substring

print(name.isalpha()) # True, returns True if all characters in the string are alphabetic

print(name.isdigit()) # False, returns True if all characters in the string are digits

print(name.startswith('G')) # True, returns True if the string starts with the specified prefix


# conditional statements
age = 20
if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult')


x ='hello'
y = 3
print(x * y) # hellohellohello , string repetition


# equality operator
a = 5
b = 5
if a == b:
    print('a and b are equal')

else:
    print('a and b are not equal')

# '!=' operator checks for inequality

a= 'Hello'
b= 'hello'
if a != b:
    print('a and b are not equal')
else:
    print('a and b are equal')


print(a > b) # False, because 'H' has a lower ASCII value than 'h'

print(ord('a')) # 97, returns the ASCII value of the character

# or operator
age = 20
if age < 18 or age > 65:
    print('You are not eligible for the job')

# and operator
age = 20
if age >= 18 and age <= 65:
    print('You are eligible for the job')

# not operator
age = 20
if not age < 18:
    print('You are eligible for the job')

print(not True) # False
print(not (False or True)) # False

# preference of operators: not > and > or

# if-elif-else ladder
age = 20
if age < 18:
    print('You are not eligible for the job')
elif age >= 18 and age <= 65:
    print('You are eligible for the job')
else:
    print('You are not eligible for the job')

# collections: list, tuple, set, dictionary

# list

x = [1, 2, 3, 4, 5, False, 'Hello'] # list
print(x) # [1, 2, 3, 4, 5, False, 'Hello']

print(x[0]) # 1, list indexing starts from 0

print(x[-1]) # 'Hello', negative indexing starts from -1

print(x[1:4]) # [2, 3, 4], list slicing, returns a new list from index 1 to 3

print(x[::2]) # [1, 3, 5, 'Hello'], list slicing with step, returns a new list with every 2nd element

print(x[::-1]) # ['Hello', False, 5, 4, 3, 2, 1], list slicing with step -1, returns a new list with elements in reverse order

print(len(x)) # 7, returns the number of elements in the list

x.append('World') # adds 'World' to the end of the list
print(x) # [1, 2, 3, 4, 5, False, 'Hello', 'World']

x.extend([6, 7, 8]) # adds multiple elements to the end of the list
print(x) # [1, 2, 3, 4, 5, False, 'Hello', 'World', 6, 7, 8]

x.insert(0, 'Start') # adds 'Start' at index 0
print(x) # ['Start', 1, 2, 3, 4, 5, False, 'Hello', 'World', 6, 7, 8]

x.pop() # removes the last element from the list
print(x) # ['Start', 1, 2, 3, 4, 5, False, 'Hello', 'World', 6, 7]

x.pop(0) # removes the element at index 0
print(x) # [1, 2, 3, 4, 5, False, 'Hello', 'World', 6, 7]

x[0] = 'John' # changes the element at index 0 to 'John'
print(x) # ['John', 2, 3, 4, 5, False, 'Hello', 'World', 6, 7]



# tuple - same as list but immutable, #*cannot be changed after creation
y = (1, 2, 3, 4, 5, False, 'Hello') # tuple
print(y) # (1, 2, 3, 4, 5, False, 'Hello')

print(y[0]) # 1, tuple indexing starts from 0
print(y[-1]) # 'Hello', negative indexing starts from -1

print(y[1:4]) # (2, 3, 4), tuple slicing, returns a new tuple from index 1 to 3

#y[-1] = 'World' # TypeError: 'tuple' object does not support item assignment, tuples are immutable
