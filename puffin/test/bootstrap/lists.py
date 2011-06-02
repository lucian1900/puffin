#!./parrot


print('test: one element list')
a = ["parrot"]
if a: print('success: one element list')
else: print('failure: one element list')

print('test: two element list')
b = ["success: two element list", ["success: subelement"]]
print(b[0])
print('test: subelement')
print(b[1][0])

print('test: single item in parens')
c = ("success: single item in parens")
print(c)

print('test: single item with comma')
d = ("success: single item with comma",)
print(d[0])

d = ["single item"]
print('test: delete from list')
del d[0]
if len(d): print('failure: delete from list')
else: print('success: delete from list')

print('test: delete list')
del a
print('success: delete list')
