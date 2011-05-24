#!./parrot pynie.pbc

# &

print('test: 1')
print('success:', (0 & 0) + 1)
print('test: 2')
print('success:', (1 & 0) + 2)
print('test: 3')
print('success:', (0 & 1) + 3)
print('test: 4')
print('success:', (1 & 1) + 3)

# |

print('test: 5')
print('success:', (0 | 0) + 5)
print('test: 6')
print('success:', (1 | 0) + 5)
print('test: 7')
print('success:', (0 | 1) + 6)
print('test: 8')
print('success:', (1 | 1) + 7)

# ^

print('test: 9')
print('success:', (0 ^ 0) + 9)
print('test: 10')
print('success:', (1 ^ 0) + 9)
print('test: 11')
print('success:', (0 ^ 1) + 10)
print('test: 12')
print('success:', (1 ^ 1) + 12)


