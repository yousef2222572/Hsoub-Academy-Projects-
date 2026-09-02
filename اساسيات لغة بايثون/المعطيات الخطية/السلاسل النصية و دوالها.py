name='hello world'
print(name[5])
print(len(name))
print('hello' in name)
print('HELLO' in name)
print(name.capitalize())
print(name.endswith('o'))
print(name.find('x'))
print(name.find('world'))
print(name.index('world'))
print(name.index('world'))
names=['ahmad','yousef','salah','salm']

spase=' '
namespase=spase.join(names)
print(namespase)

he='hello {}'
hisname=input('hello what is your name')
he_hisname=he.format(hisname)
print(he_hisname)
h='hello'
print('{0},{1},{2}' .format(h,hisname,'a good name'))
print(f'hello{hisname}')
print(f'hello {names[1]} ')