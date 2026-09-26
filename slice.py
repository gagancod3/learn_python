# slice operator #
# used to extract a portion of a list, string, or any other sequence type. 
# It allows you to specify a start index, an end index, and an optional step value.
# The syntax for slicing is as follows:

# sequence[start:end:step]

x = [1, 2, 3, 4, 5] # list
print(x) # [1, 2, 3, 4, 5]

print(x[1:4]) # [2, 3, 4], list slicing, returns a new list from index 1 to 3

print(x[::2]) # [1, 3, 5], list slicing with step, returns a new list with every 2nd element

print(x[::-1]) # [5, 4, 3, 2, 1], list slicing with step -1, returns a new list with elements in reverse order

print(x[1:5:2]) # [2, 4], list slicing with step, returns a new list with every 2nd element from index 1 to 4