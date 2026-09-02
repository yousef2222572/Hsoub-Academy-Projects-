names=['hsan','yousef','ahmad','adel']

print(names)
print(names[2])
print(names[-1])
print(names[-2])
#print(names[50])

print(names[0:2])
print(names[:2])
print(names[2:])

print(names[0::2])

print(names)
names[-1]='hade'
print(names)

names[-1]='sarah'
print(names)

names[0:2]='amera','yarah'
print(names)

names[1:3] = ''
print(names)

print('-------------------------------')
#for loop

names=['hsan','yousef','ahmad','adel']

for jhg in range(4):
    print(names[jhg])


for jhg in range(4):
    print(jhg)

for x in range (len(names)):
    print(f'im a {x} hello my name is {names[x]}')


print('-------------------------------------------------------------------------')
#enumerate
for i,x in enumerate(names):
    print(f'i am {x} and i am the {i}')

print('-----------------------------------------------------------------')
#in and not in
print('yousef' in names)

print('yousef' not in names)

print('----------------------------------------------------------------------')
"""
games=['ply station','x box','pc']

name=input('iput game name')
if name in games :
    print  ('i know this game')
else :
    print(' what you  talking about')
"""
print('-------------------------------------------------------------------------------------')
#random.choice(),random.shuffle

games=['ply station','x box','pc','']

import random

print(random.choice(games))
print(random.choice(games))
print(random.choice(games))

random.shuffle(games)
print(games)
print(random.choice(games))
print(random.choice(games))
print(random.choice(games))