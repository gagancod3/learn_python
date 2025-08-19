# SCOPES



# closures

x = 10

def f1():
    x = 20
    def f2():
        print(x)
    return f2


# we can declare the function call to a variable anywhere down the code
# What we see is that we're able to get the f2() definition as well as the 
# lexical environment of it as it accesses the 'x = 20' 
# This is closures in Python

res = f1()
res()

'''
A closure is formed when:

> An inner function references variables from its enclosing scope.

> The inner function "remembers" those variables even after the outer function has finished execution

Here:

f2 is the inner function.

It references x from f1’s scope (x = 20).

Even though f1 has finished running, the variable x is preserved in f2’s closure.

'''

def outer_fn(num):
    def actual(x):
        return x ** num
    return actual

# print(outer_fn(2)) # <function outer_fn.<locals>.actual at 0x000001F2A6178540>
f = outer_fn(2)
print(f(3)) # 3 **2 = 9

# g = outer_fn(3) 

