#!./parrot pynie.pbc
# -*- coding: utf-8 -*-

# turn on debug so assert works
__debug__ = 1     # XXX not valid in real Python.

#len
print('test: len')
n = len([1,2,3,4])
if n == 4: print('success: len')
else: print('failure: len')

#list
print('test: list')
lst1 = [ 1,2,3,4 ]
lst2 = list(lst1)
lst1.pop()
lst1.pop()
lst1.pop()
lst1.pop()
if lst2[2] == 3: print('success: list')
else: print('failure: list')

#range
print('test: range')
lst = list(range(4))
ok = 0
n = -1
for i in lst:
    n += 1
    if n == i: ok += 1
if ok == 4: print('success: range')
else: print('failure: range')

#str
print('test: str')
if str(5) == '5': print('success: str')
else: print('failure: str')

print('test: len/str')
if len(str(861)) == 3: print('success: len/str')
else: print('failure: len/str')

#max
print('test: max (simple)')
if max(range(5)) == 4: print('success: max (simple)')
else: print('failure: max (simple)')

print('test: max (mixed)')
if max([1,98,3,8,32,8]) == 98: print('success: max (mixed)')
else: print('failure: max (mixed)')

#min
print('test: min (simple)')
if min(range(5)) == 0: print('success: min (simple)')
else: print('failure: min (simple)')

print('test: min (mixed)')
if min([98,1,3,8,32,8]) == 1: print('success: min (mixed)')
else: print('failure: min (mixed)')

#ord
print('test: ord')
if ord('a') == 97: print('success: ord')
else: print('failure: ord')

#pow
print('test: pow (2 args)')
if pow(2,3) == 8: print('success: pow (2 args)')
else: print('failure: pow (2 args)')

print('test: pow (3 args)')
if pow(2,3,3) == 2: print('success: pow (3 args)')
else: print('failure: pow (3 args)')

#sum
print('test: sum')
if sum(range(5)) == 10: print('success: sum')
else: print('failure: sum')

#repr
print('test: repr (int)')
if repr(5) == '5': print('success: repr (int)')
else: print('failure: repr (int)')

print('test: repr (string)')
if repr('hi') == "'hi'": print('success: repr (string)')
else: print('failure: repr (string)')

print('test: repr (list)')
a = [ 1, 2, 'hi' ]
repr_a = "[1, 2, 'hi']"
if repr(a) == repr_a: print('success: repr (list)')
else: print('failure: repr (list)')

#map
print('test: map (builtin func)')
a = [ 1, 2, 3, 4 ]
b = [ '1', '2', '3', '4' ]
res = map(str, a)
ok = 1
for i in range(4):
    if res[i] != b[i]: ok = 0
if ok: print('success: map (builtin func)')
else:  print('failure: map (builtin func)')

print('test: map (python func)')
try:
    a = [ 1, 2, 3, 4 ]
    b = [ 2, 3, 4, 5 ]
    def f(x): return x + 1
    res = map(f, a)
    for i in range(4):
        assert res[i] == b[i]
    print('success: map (python func)')
except:
    print('failure: map (python func)')

#hex
print('test: hex')
try:
    a = [ 0, 5, -256, 1000 ]
    b = [ '0x0', '0x5', '-0x100', '0x3e8' ]
    res = map(hex, a)
    for i in range(4):
        assert res[i] == b[i]
    print('success: hex')
except:
    print('failure: hex')

#type
print('test: type')
try:
    assert type('foo') is type('yum')
    assert type('foo') is not type(5)
    assert type(8) is type(5)
    print('success: type')
except:
    print('failure: type')
