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

