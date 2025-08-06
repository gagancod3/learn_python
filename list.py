# Data structure 
# List #

# A list in Python is an ordered, mutable (changeable) collection that can contain elements of different data types.
## CHARACTERISTICS ##
# Ordered: Elements have a defined order.
# Mutable: Elements can be modified.
# Heterogeneous: Supports mixed data types.
# Indexed: Supports positive and negative indexing.
# Allow Duplicates - Since lists are indexed, lists can have items with the same value

my_list = [10, 20, "Hello", 3.14, True]

print(my_list[1])
print(my_list[-3])
print(len(my_list))

# Slicing #
# new copy of list is created
# [startIndex : endIndex(excluded)]
print(my_list[0:3])
sliced_list = my_list[0:4]
print(sliced_list)

## wrong way of adding elements in list using slicing##
# my_list[1:2] = 'Gagan'  
# print(my_list) # [10, 'G','a','g','a','n', 'Hello', 3.14, True]

# Correct way of adding elements in list using slicing
# We can replace a slice of the list with another list or a single element wrapped in a list.
# This will replace the elements at index 1 with 'Gagan'
my_list[1:2] = ['Gagan']
print(my_list) # [10, 'Gagan', 'Hello', 3.14, True]

# assigning - does not create a new copy of the list. 
# It only creates a new reference (alias) to the same list object in memory.
new_list = my_list 

# if you want to create a new copy, you can ustilize copy() method
# new_list = my_list.copy()
# or use slicing
# new_list = my_list[:]

my_list_copy = my_list.copy()
my_list.append('Python')
print(my_list) # [10, 'Gagan', 'Hello', 3.14, True, 'Python']
print(my_list_copy, 'list copy') #[10, 'Gagan', 'Hello', 3.14, True]

new_list[0] = 'Ball'
print(new_list) # ['Ball', 20, 'Hello', 3.14, True]
print(my_list) # ['Ball', 20, 'Hello', 3.14, True]

# Both lists are updated even though we only updated the new_list
# this happened bcz memory location of 'my_list' is shared to 'new_list' 
# when it's assigned with 'my_list'


# Matrix
matrix = [[1,0,1],[0,1,0],[1,0,1]]
print(matrix[0][2]) # 1

# Methods

# Length
print(len(my_list))

# append
my_list.append(100)
my_list.append('Ball')
print(my_list) # ['Ball', 20, 'Hello', 3.14, True, 100, 'Ball']

# remove 
my_list.remove('Ball')
print(my_list) #[20, 'Hello', 3.14, True, 100, 'Ball']


# pop()
# pop() - default Index is '-1' but we can specify the index as well
my_list.pop()
my_list.pop(2)
print(my_list) # [20, Hello, True, 100]

# clear() - empties the list

new_list1 = my_list.pop() # returns the popped value 
new_list2 = my_list.append('Baseball') # returns None
new_list3 = my_list.remove('Hello') # returns None
new_list4 = my_list.clear() # returns None

print(new_list1) # 100
print(new_list2) # None
print(new_list3) # None
print(new_list4) # None

print(my_list) # []

my_second_list = ['Gagan', 4 ,'Ball', 7 , 1.002, 14, 7]
# count() - counts the occurance of the value
print(my_second_list.count(7)) # 2
# 'in' returns boolean value
print('Gagan' in my_second_list) # True

# index() - returns the first index
print(my_second_list.index(7)) # 3

# sort() - will work for lists having same data types
# print(my_second_list.sort()) # ERROR

my_int_list = [3,1,7,14,5,29,33,8,79]
my_int_list.sort()
print(my_int_list) # [1, 3, 5, 7, 8, 14, 29, 33, 79]

# reverse() OR sort(reverse = True)
my_int_list.reverse()
# my_int_list.sort(reverse = True)

print(my_int_list) # [79, 33, 29, 14, 8, 7, 5, 3, 1]

# range(startIndex, endIndex(excluded) )
print(list(range(1,10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# join()
sentence = '_'
new_sentence = sentence.join(['hello','there', 'my', 'name', 'is', 'Gagan'])
print(new_sentence) # hello_there_my_name_is_Gagan

# List unpacking

a,b,c,d , *other, e = [1,2,3,4,5,6,7,8,9,10]

print(a) # 1
print(b) # 2
print(c) # 3
print(d) # 4
print(other) # [5,6,7,8,9]
print(e) # 10

# None
# In Python, None is a special constant that represents the absence of a value or a null value.

print(type(None)) # <class 'NoneType'>

# None is not 0, False, or an empty string/list — it's a distinct object.
# Used to indicate no value, no result, or not yet initialized


