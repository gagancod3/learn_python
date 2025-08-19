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

