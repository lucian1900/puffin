#!./parrot pynie.pbc

# unary operators

print('test: prefix +')
x = +7
if x == 7: print('success: prefix +')
else:
    print('failure: prefix + [')
    print("op-math-compare.py:92:FAIL test expected 7, not", end=' ')
    print(x)
    print("]")

print('test: prefix -')
x = -8
if x == -8: print('success: prefix -')
else:
    print('failure: prefix - [')
    print("op-math-compare.py:92:FAIL test expected -8, not", end=' ')
    print(x)
    print("]")

# basic math operators

print('test: addition')
x = 1 + 1
if x == 2: print('success: addition')
else:
    print('failure: addition [')
    print('02-op-math.py:7:FAIL test expected 2, not', end=' ')
    print(x)
    print(']')

print('test: addition with zero')
x = 0 + 1
if x == 1: print('success: addition with zero')
else:
    print('failure: addition with zero [')
    print('02-op-math.py:16:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

print('test: subtraction')
x = 4 - 1
if x == 3: print('success: subtraction')
else:
    print('failure: subtraction [')
    print('02-op-math.py:24:FAIL test expected 3, not', end=' ')
    print(x)
    print(']')

print('test: multiplication')
x = 2 * 2
if x == 4: print('success: multiplication')
else:
    print('failure: multiplication [')
    print('02-op-math.py:33:FAIL test expected 4, not', end=' ')
    print(x)
    print(']')

print('test: division')
x = 10 / 5
if x == 2: print('success: division')
else:
    print('failure: division [')
    print('02-op-math.py:42:FAIL test expected 2, not', end=' ')
    print(x)
    print(']')

# //, << and >>  operators

print('test: floor division')
x = 10 // 2
if x == 5: print('success: floor division')
else:
    print('failure: floor division [')
    print('02-op-math.py:53:FAIL test expected 5, not', end=' ')
    print(x)
    print(']')

print('test: floor division and addition')
x = 0 // 1 + 8
if x == 8: print('success: floor division and addition')
else:
    print('failure: floor division and addition [')
    print('02-op-math.py:62:FAIL test expected 8, not', end=' ')
    print(x)
    print(']')

print('test: left shift')
x = 3 << 1
if x == 6: print('success: left shift')
else:
    print('failure: left shift [')
    print('02-op-math.py:71:FAIL test expected 6, not', end=' ')
    print(x)
    print(']')

print('test: right shift')
x = 14 >> 1
if x == 7: print('success: right shift')
else:
    print('failure: right shift [')
    print('02-op-math.py:80:FAIL test expected 7, not', end=' ')
    print(x)
    print(']')

# ** operator

print('test: power')
x = 3 ** 2
if x == 9: print('success: power')
else:
    print('failure: power [')
    print('02-op-math.py:91:FAIL test expected 9, not', end=' ')
    print(x)
    print(']')

print('test: 0 to the power of 0')
x = 0 ** 0
if x == 1: print('success: 0 to the power of 0')
else:
    print('failure: 0 to the power of 0 [')
    print('02-op-math.py:104:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

print('test: 0 to the power of 1')
x = 0 ** 1
if x == 0: print('success: 0 to the power of 1')
else:
    print('failure: 0 to the power of 1 [')
    print('02-op-math.py:109:FAIL test expected 0, not', end=' ')
    print(x)
    print(']')

print('test: 1 to the power of 0')
x = 1 ** 0
if x == 1: print('success: 1 to the power of 0')
else:
    print('failure: 1 to the power of 0 [')
    print('02-op-math.py:118:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

# unary + and -
print('test: unary plus')
x = +13
if x == 13: print('success: unary plus')
else:
    print('failure: unary plus [')
    print('02-op-math.py:128:FAIL test expected 13, not', end=' ')
    print(x)
    print(']')

# unary + and -
print('test: unary minus')
x = -10 + 24
if x == 14: print('success: unary minus')
else:
    print('failure: unary minus [')
    print('02-op-math.py:128:FAIL test expected 14, not', end=' ')
    print(x)
    print(']')
