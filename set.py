## Data Structure ##

# Set #

# CHARACTERISTICS #
# Unordered, Mutable (changeable), and unindexed (unlike arrays/list) collection of unique elements (no duplicates)
# No duplicate values.
# No indexing or slicing.
# Elements must be immutable (e.g., numbers, strings, tuples).

# We can utilize this data structure when storing unique (non-duplicate) values
# like Email ID or username

# Empty set must be declared using 'set()'

empty_set = set()
print(empty_set) # set()

my_set_one = set()

# Adding elements
my_set_one.add(7)
my_set_one.add(14)
my_set_one.add(21)
my_set_one.add(10)
my_set_one.add(10)

print(my_set_one) # {10, 21, 14, 7}

''' 
In Python, sets are unordered collections, which means they do not preserve insertion order
like lists or dictionaries (prior to Python 3.7). However, as of Python 3.7+, the insertion
order is preserved in practice, but you should not rely on it, as sets are still officially
documented as unordered.

> Python uses a hashing algorithm to store set elements.

> When elements are added, they are stored in hash table buckets based on their hash values.

> This is why the output order may seem arbitrary or different from the insertion order.
'''  

# Remove elements (Raises error if not present)
my_set_one.remove(21) 
# discard() work same as remove() 
my_set_one.discard(10)
# Final output of set
print(my_set_one) # {14, 7}

# copy() set
copied_set = my_set_one.copy()
print(copied_set) # {14, 7}

# empty the set (checking for the reference of copied set)
my_set_one.clear()
print(my_set_one) # set()
print(copied_set) # {14, 7}

# convert list into set (where it removes duplicates)
my_list = [1,2,3,4,5,5]
print(set(my_list)) # {1,2,3,4,5}
# print(my_set[0]) # Error 

# Methods 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Return a new set with elements in the set that are not in the others
print(my_set.difference(your_set)) # {1, 2, 3} 
# O/P - {1, 2, 3} aren't present in the 'your_set'

# "Update the set", removing elements found in others.
# print(my_set.difference_update(your_set)) # None
# print(my_set) # {1, 2, 3}

# Return a new set with elements common to the set and all others.
intersect_set = my_set.intersection(your_set)
print(intersect_set) # {4, 5}

# Return True if two sets have a null intersection.
print(my_set.isdisjoint(your_set)) # False

# Report whether another set contains this set.
print(my_set.issubset(your_set)) # False 

# Report whether this set contains another set.
print(my_set.issuperset(your_set)) # False

# Union - Return a new set with elements from the set and all others.
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

subset_set = {4, 5, 6}

print(subset_set.issubset(your_set)) # True
print(your_set.issuperset(subset_set)) # True

