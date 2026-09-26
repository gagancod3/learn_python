# comprehensions #

# Used for easy declaration in one single line

x = [x for x in range(5)]

print(x) # [0,1,2,3,4]

y = [y+2 for y in range(5)]
print(y) # [2,3,4,5,6]

z = [[0 for z in range(5)] for z in range(2)]
print(z)