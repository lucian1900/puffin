#!./parrot

print('test: len')
a = [1,2,3]
if len(a) == 3: print('success: len')
else: print('failure: len')

print('test: equality')
a = [0, 1, 2]
if a == [0, 1, 2] and a != [7, 8, 9]: print('success: equality')
else: print('failure: equality')

print('test: append')
a = []
for i in range(3): a.append(i)
if a == [0, 1, 2]: print('success: append')
else: print('failure: append')

print('test: count')
a = [1,2,5,6,5,5,5,5,6]
if a.count(5) == 5 and a.count(6) == 2: print('success: count')
else: print('failure: count')

print('test: extend')
a = [0, 1, 2]
b = [7, 8, 9]
a.extend(b)
# b should be added to a, but should not be affected
if a == [0, 1, 2, 7, 8, 9] and b == [7, 8, 9]: print('success: extend')
else: print('failure: extend')

print('test: index')
a = [5,8,7]
# XXX check for ValueError if value doesn't exist
if a.index(8) == 1: print('success: index')
else: print('failure: index')

print('test: insert')
a = [0, 1, 2]
a.insert(1, 8)
if a == [0, 8, 1, 2]: print('success: insert')
else: print('failure: insert')

print('test: pop')
a = [0, 1, 2]
i = a.pop()     # pop the 2
j = a.pop(0)    # pop the 0
if i == 2 and j == 0: print('success: pop')
else: print('failure: pop')

print('test: remove')
a = [5,8,7]
# XXX check for ValueError if value doesn't exist
a.remove(8)
if a == [5, 7]: print('success: remove')
else: print('failure: remove')

print('test: reverse (empty)')
a = []
a.reverse()
if a == []: print('success: reverse (empty)')
else: print('failure: reverse (empty)')

print('test: reverse (even element count)')
a = [1, 2, 3, 4, 5, 6]
a.reverse()
if a == [6,5,4,3,2,1]: print('success: reverse (even element count)')
else: print('failure: reverse (even element count)')

print('test: reverse (odd element count)')
a = [1, 2, 3, 4, 5]
a.reverse()
if a == [5,4,3,2,1]: print('success: reverse (odd element count)')
else: print('failure: reverse (odd element count)')

print('test: str(list)')
a = [0, 1, 2]
if str(a) == '[0, 1, 2]': print('success: str(list)')
else: print('failure: str(list)')

print('test: repr(list)')
a = [0, 1, 2]
if repr(a) == '[0, 1, 2]': print('success: repr(list)')
else: print('failure: repr(list)')
