
# Handling Exceptions #

try:
    x = 7/0
except Exception as e:
    print(e) # division by zero

finally:
    print('finally block')