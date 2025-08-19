## Data Structure ##
# Tuple #

# Ordered: Elements have a fixed position.
# Immutable: Cannot be changed after creation. (Unchangeable)
# Supports heterogeneous data types.
# Allows 'indexing' and 'slicing'.
# Faster than lists
# Allows duplicates since indexed

my_tuple = (10, "Gagan", 3.14, True)
print(my_tuple)
# single-element tuple

#Let's try with single element
single = (5)
print(single) # 5
print(type(single)) # <class 'int'>

# above scenario, it considers it as a integer value

# now we'll add a ',' comma at the end

single_tuple = (5,)
print(single_tuple) # (5,)
print(type(single_tuple)) # <class 'tuple'>
# here it considers it as a tuple

# Slicing
print(my_tuple[1:3])    # ('Gagan', 3.14)


# for loop 
for item in my_tuple:
    print(item)


# Count and index
t = (1, 2, 2, 3)
print(t.count(2))       # 2
print(t.index(3))       # 3

# Destructuring
person = ("John", 25, "Engineer")

name, age, profession = person

print(name)       # John
print(age)        # 25
print(profession) # Engineer
