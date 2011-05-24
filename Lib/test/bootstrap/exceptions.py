#!./parrot pynie.pbc

print('test: catch exception')
try:
    x = 1
    raise Exception
except:
    x = 2
if x == 2: print('success: catch exception')
else: print('failure: catch exception')

print('test: no exception')
try:
    x = 1
except:
    x = 2
if x == 1: print('success: no exception')
else: print('failure: no exception')

# make sure asserts are on
# XXX in real Python, you can't set __debug__
# fix this test so it doesn't either

__debug__ = 1

print('test: assert false')
try:
    x = 1
    assert 0
except:
    x = 2
if x == 2: print('success: assert false')
else: print('failure: assert false')

print('test: assert true')
try:
    x = 1
    assert 1
except:
    x = 2
if x == 1: print('success: assert true')
else: print('failure: assert true')

print('test: assert false, no debug')
__debug__ = 0
try:
    x = 1
    assert 0
except:
    x = 2
if x == 1: print('success: assert false, no debug')
else: print('failure: assert false, no debug')
