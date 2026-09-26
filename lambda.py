# lambda function #

# anonymous function, one liner

x = lambda a, b: a+b
print(x(2,3)) # 5


# Used in Map & filter 

y = [1,2,3,4,5,6,7,8,9,10]
res_map = map(lambda i: i * 2, y)  # map object
print(list(res_map)) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



res_filter = filter(lambda i: i % 2 == 0, y)  # map object
print(list(res_filter)) # [2, 4, 6, 8, 10]