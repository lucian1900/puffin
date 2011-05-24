#!./parrot pynie.pbc

# &

print('test: boolean logic 0 AND 0')
x = 0 & 0
if x == 0: print('success: boolean logic 0 AND 0')
else:
    print('failure: boolean logic 0 AND 0 [')
    print('03-op-logic.py:6:FAIL test expected 0, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 0 AND 1')
x = 0 & 1
if x == 0: print('success: boolean logic 0 AND 1')
else:
    print('failure: boolean logic 0 AND 1 [')
    print('03-op-logic.py:15:FAIL test expected 0, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 1 AND 0')
x = 1 & 0
if x == 0: print('success: boolean logic 1 AND 0')
else:
    print('failure: boolean logic 1 AND 0 [')
    print('03-op-logic.py:24:FAIL test expected 0, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 1 AND 1')
x = 1 & 1
if x == 1: print('success: boolean logic 1 AND 1')
else:
    print('failure: boolean logic 1 AND 1 [')
    print('03-op-logic.py:33:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

# |

print('test: boolean logic 0 OR 0')
x = 0 | 0
if x == 0: print('success: boolean logic 0 OR 0')
else:
    print('failure: boolean logic 0 OR 0 [')
    print('03-op-logic.py:6:FAIL test expected 0, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 0 OR 1')
x = 0 | 1
if x == 1: print('success: boolean logic 0 OR 1')
else:
    print('failure: boolean logic 0 OR 1 [')
    print('03-op-logic.py:15:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 1 OR 0')
x = 1 | 0
if x == 1: print('success: boolean logic 1 OR 0')
else:
    print('failure: boolean logic 1 OR 0 [')
    print('03-op-logic.py:24:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')

print('test: boolean logic 1 OR 1')
x = 1 | 1
if x == 1: print('success: boolean logic 1 OR 1')
else:
    print('failure: boolean logic 1 OR 1 [')
    print('03-op-logic.py:33:FAIL test expected 1, not', end=' ')
    print(x)
    print(']')
