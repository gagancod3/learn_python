# Truthy & Falsy #

val_emptyString = ''
val_string = 'hey'
val_zero = 0 
val_nonzero = 7
val_nonzero_decimal = 0.007

print(bool(val_emptyString)) # False
print(bool(val_string)) # True
print(bool(val_zero)) # False
print(bool(val_nonzero)) # True
print(bool(val_nonzero_decimal)) # True

# Ternary Operator #
val_a = 'adult'
val_b = 'below 18'
val_c = 21

result = val_a if val_c >= 18 else val_b
print(result) # adult

# Short Circuiting #

is_friend = True
is_user = True

if is_friend or is_user:
    print('case1:','best friends forever')
if is_friend and is_user:
    print('case2:','best friends forever')

#  In above both cases, we see it's true
#  When used 'OR' operator if first operand is True, it returns 'True' without checking second operand
#  This is 'Short-circuiting' 
#  But in case, first operand is False then it checks second operand

#  Contrastingly, when used 'AND' operator if first operator is False, it returns 'False' without checking second operand

# Logical Operator #

is_magician = True
is_expert = False

if is_expert and is_magician: 
    print("You're a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("You need magic powers")

# print(bool(0))

print(True == 1) #True
print('' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True

print(True is 1) # False
print([1,2,3] is [1,2,3]) #False #allocated different location
print([] is []) # False #allocated different location

print(True is True) # True
print('1' is '1') #True


# powered_num 

squared_num = [num**2 for num in range(11)]
print(squared_num) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubed_num = [num**3 for num in range(11)]
print(cubed_num) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]