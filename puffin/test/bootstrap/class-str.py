#!./parrot

print('test: str.split')
if 'foobar'.split('o') == [ 'f', '', 'bar' ]:
    print('success: str.split')
else:
    print('failure: str.split')

print('test: str.join')
if '---'.join(['hello', 'world']) == 'hello---world':
    print('success: str.join')
else:
    print('failure: str.join')
