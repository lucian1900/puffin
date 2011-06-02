#!./parrot pynie.pbc

print('test: logical AND true')
if 1 and 2 and 3:
    print('success: logical AND true')
else:
    print('failure: logical AND true')

print('test: logical AND false')
if 0 and 1 and 2:
    print('failure: logical AND false')
else:
    print('success: logical AND false')

print('test: logical OR true')
if 0 or 1 or 2:
    print('success: logical OR true')
else:
    print('failure: logical OR true')

print('test: logical OR false')
if 0 or 0 or 0:
    print('failure: logical OR false')
else:
    print('success: logical OR false')

print('test: logical NOT true')
if not 0:
    print('success: logical NOT true')
else:
    print('failure: logical NOT true')

print('test: logical NOT false')
if not 1:
    print('failure: logical NOT false')
else:
    print('success: logical NOT false')

print('test: logical OR/AND precedence')
if 1 or 0 and 0:   # and should be tighter than or
    print('success: logical OR/AND precedence')
else:
    print('failure: logical OR/AND precedence')

print('test: logical ops parentheses')
if (1 or 0) and 0:   # test parentheses
    print('failure: logical ops parentheses')
else:
    print('success: logical ops parentheses')

print('test: double NOT')
#if not not 1:
#   print 'success: double NOT'
#else:
#   print 'failure: double NOT'
print('xfail: double NOT [')
print('fix double nots')
print(']')

print('test: conditional expressions')
if 5 == (5 if 1 else 8) and 8 == (5 if 0 else 8):
    print('success: conditional expressions')
else:
    print('failure: conditional expressions')
