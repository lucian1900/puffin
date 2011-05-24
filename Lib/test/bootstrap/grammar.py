#!./parrot pynie.pbc

print('test: backslash for line continuation')
x = 1 \
+ 1
if x != 2:
    print('failure: backslash for line continuation [')
    print("test_grammar.py:9:FAIL test expected 2, not", end=' ')
    print(x)
    print("]")
else: print('success: backslash for line continuation')

print('test: backslash ending comment')
# Backslash in comments :\
x = 0
if x != 0:
    print('failure: backslash ending comment [')
    print("test_grammar.py:16:FAIL test expected 0, not", end=' ')
    print(x)
    print("]")
else: print('success: backslash ending comment')


print('test: backslash ending comment after space')
# Backslash in comments \
x = 2
if x != 2:
    print('failure: backslash ending comment after space [')
    print("test_grammar.py:27:FAIL test expected 2, not", end=' ')
    print(x)
    print("]")
else: print('success: backslash ending comment after space')


print('test: hex int')
if 0xff != 255:
    print('failure: hex int [')
    print("test_grammar.py:36:FAIL test expected 255, not", end=' ')
    print(0xff)
    print("]")
else: print('success: hex int')

print('test: octal int')
if 0o377 != 255:
    print('failure: octal int [')
    print("test_grammar.py:44:FAIL test expected 255, not", end=' ')
    print(0o377)
    print("]")
else: print('success: octal int')
