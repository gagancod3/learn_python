def square_num(num):
    print(num ** 2)
    return num ** 2

result = square_num(5)  # Output: 25

# when no return statement is present
print(result)  # Output: "None", since the function does not return anything

# when a return statement is present
result = square_num(7)  # Output: 25
print(result)  # Output: 25, since the function returns the square of the number

def add_numbers(a, b):
    return a + b

result = add_numbers(3,4)  # Output: 7

# Polymorphism in functions
def multiply(p1, p2):
    return p1 * p2

print(multiply(5,8)) # 40
print(multiply('G',5)) # GGGGG
print(multiply(5,'P')) # PPPPP

# Function returning multiple values

import math

def circle_stats(radius):
    area = round(math.pi, 3) * radius ** 2
    circumference = 2 * math.pi * radius
    return (area, circumference)     # returning multiple values

# print(circle_stats(7))

area_circle, circumference_circle = circle_stats(3) 
print(area_circle)
print(circumference_circle)


def func(x, y, z=None):
    print('Run', x, y, z)
    return x*y, x/y

r1, r2 = func(5,6,7)  # destructure / unpacking
print(r1) # 30
print(round(r2, 2)) # 0.83
print(r1,r2) # 30 0.833334


abc = [1,2,3,4,5]
#a,b,c = abc  # ValueError: too many values to unpack

# function returning another function

def parent(x):
    def child():
        print(f'value {x} is printed from child function')
    return child

print(parent(7)) # reference to the inner function 'child'

parent(7)() # value 7 is printed from child function

# *args and **kwargs - let a function accept a variable number of agruments

# *args -> stored as a tuple
# **kwargs -> stored as a dictionary

x = [1,2,34,56,778]
y = {'name':'Karan', 'age': 25}

print(x) # [1, 2, 34, 56, 778]
print(*x) # 1 2 34 56 778

def add(*args):
    print(args) # (1, 2, 3, 4)

add(1, 2, 3, 4)

def dict_arg(x,y):

    print(x,y) # 2 5

dict_arg(**{'y':5, 'x':2})

def func(*args, **kwargs):
    print(args,kwargs) # (1, 2, 34, 56, 778) {'name': 'Karan', 'age': 25}
    return

func(1,2,34,56,778,name='Karan',age=25)
