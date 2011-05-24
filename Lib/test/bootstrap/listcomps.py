#!./parrot


print('test: simple list comp.')
a = [ i + 3 for i in range(3) ]
if a == [ 3, 4, 5 ]: print('success: simple list comp.')
else: print('failure: simple list comp.')

print('test: list comp. with if')
a = [ i for i in range(6) if i > 3 ]
if a == [ 4, 5 ]: print('success: list comp. with if')
else: print('failure: list comp. with if')

print('test: complex list comp.')
a = [ (i,10+j) for i in range(3) if i > 0 for j in range(4) if j < 3 if j > 0 ]
if a == [(1, 11), (1, 12), (2, 11), (2, 12)]:
    print('success: complex list comp.')
else:
    print('failure: complex list comp.')

print('test: nested list comp.')
a = [ [ i + 2 for i in range(j) ] for j in range(3) ]
if a == [ [], [2], [2,3] ]:
    print('success: nested list comp.')
else:
    print('failure: nested list comp.')
