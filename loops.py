# FOR #

for a in range(10):
    # block of code
    print(a) # 0 1 2 3 4 5 6 7 8 9


for i in [1,2,3]:
    print(i) # 1 2 3


# start, stop, step
# for i in range(start, stop, step)

#* start is always included, stop is always excluded, step is optional and default is 1
#* start should be less than stop if step is positive, start should be greater than stop if step is negative

for i in range(1, 10, 2):
    print(i) # 1 3 5 7 9

for i in range(10, 0, -1):
    print(i) # 10 9 8 7 6 5 4 3 2 1

for i in range(10, 0, -2):
    print(i) # 10 8 6 4 2

print('running a loop in reverse order')
for i in range(-10, -1, -1):
    print(i) # empty since -10 is less than -1, so the loop will not run


# While #
a = 1
n = 4
while a < n:
    print(f'{a} still less than {n}')
    a = a + 1 # incrementing a by 1 we can also write #* (a += 1)

# same thing can be done like
while True:
    print(f'{a} still less than {n}')
    a = a + 1
    if a >= n:
        break


for i in range(5):
    if i == 3:
        break
    print(i) # 0 1 2




