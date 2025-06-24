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

# Unlike lists where we can have array of objects

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

