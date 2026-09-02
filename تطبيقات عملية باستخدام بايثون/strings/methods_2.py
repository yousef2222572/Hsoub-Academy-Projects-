#startswith,endswith

test='Hello world'
print(test.startswith('Hello'))
print(test.startswith('world'))

print(test.endswith('Hello'))
print(test.startswith('world'))






print(test.startswith('H'))
print(test.startswith('w'))

print(test.endswith('H'))
print(test.startswith('w'))
print(test.startswith('w',6,11))
print('-----------------------------------------------------')
#strip, rstrip ,lstrip

test='  hello world   '
print(test)
print(test.strip())
print(test.lstrip())
print(test.rstrip())

test='@@hello world@@'
print(test.strip('@'))
print(test.lstrip('@'))
print(test.rstrip('@'))


test='@#@#hello world@#@#'
print(test.strip('#@'))
print(test.lstrip('#@'))
print(test.rstrip('#@'))

print('------------------------------------------------------')


#zfill

hours='1'
min='21'
sec='5'

print(f'{hours}{min}{sec}')
print(f'{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')
print(f'{hours.zfill(2)}:{min.zfill(3)}:{sec.zfill(2)}')


















