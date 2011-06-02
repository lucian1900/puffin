#!./parrot pynie.pbc

print('test: 0 less than 1')
if 0 < 1: print('success: 0 less than 1')

print('test: 1 greater than 0')
if 1 > 0: print('success: 1 greater than 0')

print('test: 0 less than/equal 1')
if 0 <= 1: print('success: 0 less than/equal 1')

print('test: 0 less than/equal itself')
if 0 <= 0: print('success: 0 less than/equal itself')

print('test: 1 greater than/equal 0')
if 1 >= 0: print('success: 1 greater than/equal 0')

print('test: 0 greater than/equal itself')
if 0 >= 0: print('success: 0 greater than/equal itself')

print('test: 0 less than 1, less than 2')
if 0 < 1 < 2: print('success: 0 less than 1, less than 2')

print('test: 2 greater than 1, greater than 0')
if 2 > 1 > 0: print('success: 2 greater than 1, greater than 0')

print('test: is operator - compare int with self')
a = 1000
if a is a:
    print('success: is operator - compare int with self')
else:
    print('failure: is operator - compare int with self')

print('test: is operator - compare 2 ints')
a = 1000
b = 1000
if not (a is b):
    print('success: is operator - compare 2 ints')
else:
    print('failure: is operator - compare 2 ints')

print('test: is not operator - compare int with self')
a = 1000
if not (a is not a):
    print('success: is not operator - compare int with self')
else:
    print('failure: is not operator - compare int with self')

print('test: is not operator - compare 2 ints')
a = 1000
b = 1000
if a is not b:
    print('success: is not operator - compare 2 ints')
else:
    print('failure: is not operator - compare 2 ints')
