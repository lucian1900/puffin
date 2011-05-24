#!./parrot pynie.pbc

# if

print('test: if true')
if 1: print('success: if true')
else: print('failure: if true')

print('test: if false')
if 0: print('failure: if false')
else: print('success: if false')

print('test: elif true')
if 0: print('failure: elif true')
elif 1: print('success: elif true')

print('test: elif false')
if 0: print('failure: elif false')
elif 0: print('failure: elif false')
else: print('success: elif false')

# while

i=5
while i < 7:
    print('test:', i)
    print('success:', i)
    i=i+1

print('test: while count')
if i == 7: print('success: while count')
else: print('failure: while count')

print('test: while false')
while 0:
    print('failure: while false')
else:
    print('success: while false')

# for

print('test: for list literal')
n = 0
compare = 1
for i in [ 1,2,3,4 ]:
    n += 1
    if i != n: compare = 0
if compare: print('success: for list literal')
else: print('failure: for list literal')

print('test: for list assign')
lst = [ 1,2,3,4 ]
n = 0
compare = 1
for i in lst:
    n += 1
    if i != n: compare = 0
if compare: print('success: for list assign')
else: print('failure: for list assign')

print('test: for list bare')
n = 0
compare = 1
for i in 1,2,3,4:
    n += 1
    if i != n: compare = 0
if compare: print('success: for list bare')
else: print('failure: for list bare')

print('test: nested fors')
lst = [ ]
for i in range(3):
    for j in range(3):
        lst.append((i + 1) * (j + 1))
compare = 1
lst2 = [ 1, 2, 3,  2, 4, 6,  3, 6, 9 ]
for i in range(9):
    if lst[i] != lst2[i]: compare = 0
if compare: print('success: nested fors')
else: print('failure: nested fors')

print('test: multiple iterators')
#compare = 0
#for i, j in ( (0, 0), (1, 2), (2, 4) ):
#    if j == i * 2: compare += 1
#if compare == 3: print 'success: multiple iterators'
#else: print 'failure: multiple iterators'
print('xfail: multiple iterators [')
print('multiple iterators not implemented yet')
print(']')

print('test: nested scopes')
i = 4
if 0:
    if 0: pass
    i = 2
if i == 2: print('failure: nested scopes')
else: print('success: nested scopes')

print('test: for var exists after loop')
i = 0
for i in [7,1,3]:
    pass
if i == 3: print('success: for var exists after loop')
else: print('failure: for var exists after loop')
