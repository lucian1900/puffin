#!./parrot pynie.pbc

# check augmented assignment ops

print('test: plus assign')
i = 0
i += 10
if i == 10: print('success: plus assign')
else: print('failure: plus assign')

print('test: minus assign')
i = 10
i -= 5
if i == 5: print('success: minus assign')
else: print('failure: minus assign')

print('test: multiply assign')
i = -5
i *= 2
if i == -10: print('success: multiply assign')
else: print('failure: multiply assign')

print('test: divide assign')
i = 10
i /= 2
if i == 5: print('success: divide assign')
else: print('failure: divide assign')

print('test: modulus assign')
i = 10
i %= 4
if i == 2: print('success: modulus assign')
else: print('failure: modulus assign')

print('test: exponent assign')
#i = 3
#i **= 3
#if i == 27: print 'success: exponent assign'
#else: print 'failure exponent assign'
print('xfail: exponent assign [')
print('implement **=')
print(']')

print('test: right shift assign')
i = 128
i >>= 2
if i == 32: print('success: right shift assign')
else: print('failure: right shift assign')

print('test: left shift assign')
i = 1
i <<= 10
if i == 1024: print('success: left shift assign')
else: print('failure: left shift assign')

print('test: bitwise AND assign')
i = 0x55
i &= 0x1f
if i == 0x15: print('success: bitwise AND assign')
else: print('failure: bitwise AND assign')

print('test: bitwise XOR assign')
i = 0x55
i ^= 0x1f
if i == 0x4a: print('success: bitwise XOR assign')
else: print('failure: bitwise XOR assign')

print('test: bitwise OR assign')
i = 0x55
i |= 0x1f
if i == 0x5f: print('success: bitwise OR assign')
else: print('failure: bitwise OR assign')
