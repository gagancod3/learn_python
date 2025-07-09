# common iterable types

#string
word = "hello"
#list 
list_i = [1,2,3]
#tuple
tuple_i = (1,2)
#set
set_i = {1,2,3}
#dictionary
dict_i = {"a":1, "b":2}


# iter() fn (built-in)
# converts an iterable into an iterator 
# Calls the object's __iter__() method internally
list_i = [1,2,3]
it = iter(list_i)
print(it) # <list_iterator object at 0x0000027A8D8FL2E0>
print(next(it)) # 1


# next() fn
# built-in fn
# retrieves the next item from an iterator
# Internally calls the iterator's __next__() method
# Raises StopIteration when items are exhuasted

print(next(it)) # 2
print(next(it)) # 3
# print(next(it)) # StopIteration error


# enumerate()
# built-in fn that adds a counter to an iterable and returns it as an enumerate object

# SYNTAX :
# enumerate(iterable, start=0)

for index, n in enumerate(['apple','banana','carrot'], start=0):
    print(index,n)

# 0 apple
# 1 banana
# 2 carrot


# enumerate() useful when you need both element and index while looping
# Cleaner alternative to using range(len(...))


dict_i = {"a":1, "b":2}
for item in dict_i.items():
    print(item) # ('a', 1) ('b', 2)

# we can also do 
for key, value in dict_i.items():
    print(key,value) #  a 1  b 2

for item in dict_i.values():
    print(item) # 1 2

for item in dict_i.keys():
    print(item) # a b


# break, continue & pass #

# range starts from 0 and excludes last number range(5) covers from 0 1 2 3 4

# break - immediately exits the loop;  used to stop iteration based on a condition
for i in range(5):
    if i == 3:
        break
    print(i)

# 0 1 2

# continue - skips the current iteration & moves to the next, loop doesn't exit

for i in range(5):
    if i == 3:
        continue
    print(i)

# 4

# pass - does nothing, used when a statement is syntactically reqd but no action reqd

for i in range(5):
    if i == 3:
        pass
    print(i)

# 0 1 2 3 4


# WHILE #

i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    if i == 4:
        break
    i += 1

