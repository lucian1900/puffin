#!./parrot pynie.pbc

# check literals

print('test: integer literals')
0
1
12
print('success: integer literals')


print('test: integer literals with suffix')
#123l
#1234L
print('xfail: integer literals with suffix')


print('test: octal literals')
0o1
0o2
0o3
0o4
0o5
0o6
0o7
print('success: octal literals')


print('test: hex literals')
0x1
0x2
0x3
0x4
0x5
0x6
0x7
0x8
0x9
0xa
0xA
0xb
0xB
0xc
0xC
0xd
0xD
0xe
0xE
0xf
0xF
0xdeadbeef
print('success: hex literals')

print('test: floating point literals')
#3.14
#10.
#.001
#1e100
#
#3.14e-10
#0e0
#0E0
#
print('xfail: floating point literals')


print('test:', end=' ')
print(4)
print('success:', end=' ')
print(4)


print('test: imaginary literals')
#3.14j
#10.j
#10j
#.001j
#1e100j
#3.14e-10j
#1J
print('xfail: imaginary literals')


print('test: short string literals')
'foo" '
"Foo' "
'\1\2\3'
"\4\5\6"
'\x5'
print('success: short string literals')

print('test: long string literals')
#'''foo'''
#"""foo"""
#'''\x8'''
print('xfail: long string literals')
