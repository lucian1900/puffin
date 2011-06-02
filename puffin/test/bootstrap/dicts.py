#!./parrot

print('test: one element dict')
a = {"foo":1}
if a: print('success: one element dict')
else: print('failure: one element dict')

print('test: display dict element')
b = a['foo']
if b == 1: print('success: display dict element')
else: print('failure: display dict element')

print("test: display dict {'foo': 1}")
print("success: display dict", a)

print('test: add element to dict')
a['bar'] = "baz"
b = a['bar']
if b == 'baz': print('success: add element to dict')
else: print('failure: add element to dict')

print('test: delete element from dict')
del a['bar']
if len(a) > 1: print('failure: delete element from dict')
else: print('success: delete element from dict')

#print('test: delete element from dict, in')
#if 'bar' in a: print('failure: delete element from dict, in')
#else: print('success: delete element from dict, in')

print("test: integer as index")
a = {1: 2}
b = list(a.keys())
if b[0] == 1: print('success: integer as index')
else: print('failure: integer as index')

print('test: multiple elements')
a = {1: 2, 3: 4, 5: 6}
if len(a) == 3: print('success: multiple elements')
else: print('failure: multiple elements')
