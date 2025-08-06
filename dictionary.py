## Data Structure ##
# Dictionary #

# CHARACTERISTICS

# Keys are unique and immutable (strings, numbers, tuples).
# Values can be of any data type.
# Accessed using keys, not indexes. (No arrays)

dict_one = {
    'key1': [1,2,3],
    'b': 'hey there',
    'c': True
}

print(dict_one['key1']) # [1, 2, 3]
print(dict_one['key1'][2]) # 3

print(dict_one.get('b')) # hey there

# default to iterate over keys
for i in dict_one: 
    print(i)    # key1, b, c

# explicitly iterate over keys
for i in dict_one.keys(): 
    print(i)    # key1, b, c

# explicitly iterate over values
for i in dict_one.values():
    print(i) # [1, 2, 3], hey there, True

# accessing key and value pairs with items()
for i, j in dict_one.items():
    print(i,":", j) # key1 [1, 2, 3], b hey there, c True



# here we can have array of objects
# where each object can have different keys and values
my_list =  [{
    'key1': [1,2,3],
    'b': 'hey there',
    'c': True
    },
    {
        'a': 'first value',
        'key2': [3,4,5],
        'third_key': False
    }
]

print(my_list[0]['key1']) # [1, 2, 3]
print(my_list[0]['key1'][2]) # 3


# Keys for dictionary

dict_two = {
    123: [1,2,3],
    True: 'hello',
    'HaveToUnique': True
}

print(dict_two['HaveToUnique']) # True

# Methods

dict_three = dict(name='John',age=35, city='Mumbai')
print(dict_three) 
# {'name': 'John', 'age': 28}

print('name' in dict_three) # True

print('John' in dict_three.values()) # True
print('age' in dict_three.keys()) # True

#clear() - empty dictionary

# dict_three.clear()
# print(dict_three) # {}

# pop()
print(dict_three.pop('age')) # 35
print(dict_three) # {'name': 'John', 'city': 'Mumbai'}


# print(dict_three.pop('country')) # KeyError

# from Python3.7 it removes last key:value pair from dictionary
# print(dict_three.popitem())   # ('city', 'Mumbai')


# update - if that key exist, it updates the value for that key if key is not present, it adds and give value

print(dict_three.update({'role':'developer'}))
print(dict_three) 
# {'name': 'John', 'city': 'Mumbai', 'role': 'developer'}


chai_types = {
    'masala': 'spicy', 'Green': 'healthy', 'Lemon': 'refreshing'}
print(chai_types)

chai_types.update({'Ginger': 'strong'})
print(chai_types)

chai_types.pop('masala')
print(chai_types) # {'Green': 'healthy', 'Lemon': 'refreshing', 'Ginger': 'strong'}

# Nested Dictionary
tea_types = { 'chai': {'masala': 'spicy', 'Green': 'healthy', 'Lemon': 'refreshing'},
              'tea': {'black': 'bitter', 'green': 'light', 'herbal': 'calming'}}

print(tea_types)

square_num = {x: x**2 for x in range(5)}
print(square_num) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# empty square_num
square_num.clear()
print(square_num) # {}