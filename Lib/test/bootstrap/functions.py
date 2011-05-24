#!./parrot pynie.pbc
# Copyright (C) 2009, Allison Randal
# Copyright (C) 2009, isop44
# Copyright (C) 2009, Bradley M. Kuhn <bkuhn@ebb.org>

print('test: define and call a function')
def x():
 print("success: define and call a function")

x()

print('test: a function with arguments')
def y(a,b,c):
 pass

y(1,2,3)
print('success: a function with arguments')

print('test: a function with keyword arguments')
y(1,2,c=3)
print('success: a function with keyword arguments')

print('test: simple closure with lambda')
def lambda_closure(n):
    return lambda: n
a = lambda_closure(1)
b = lambda_closure(5)
if a() == 1 and b() == 5:
    print('success: simple closure with lambda')
else:
    print('failure: simple closure with lambda')

print('test: simple closure with def')
def def_closure(n):
    def inner(): return n
    return inner
a = def_closure(1)
b = def_closure(5)
if a() == 1 and b() == 5:
    print('success: simple closure with def')
else:
    print('failure: simple closure with def')

print('test: lambda inside lambda closure')
outer = lambda x: lambda: x
c = outer(12)
d = outer(22)
if c() == 12 and d() == 22:
    print('success: lambda inside lambda closure')
else:
    print('failure: lambda inside lambda closure')


