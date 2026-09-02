"""for i in range(5):
    print(i, end= ' ')"""
name=['yousef','mahmoud','hamza','salman','omar']
for name in name:
    print(name,end= ' ')
print()
name='hello i am yousef'
for i in name:
    print(i,end=' ')
print()
num={1,2,3,4,5,6,7,8,9}
for num in num:
    print(num,end=' ')
print()
    
number={1:'one',2:'two',3:'three'}
#for nu in number.items:#or valuas or keys
#    print(nu,end=',')
print()
for k,v in number.items():
    print(f'the key is {k} and the valuas is {v}')
set=[('yousef','mahmoud')]
for a , b in set:
    print(f'first name is {a} last name is {b}')
names=['yousef','salman','ahmad','jaber']
print(names)
for num in range(len(names)):
    print(f'{num+1} the name is {names[num]}')
print('-------------------------------------------------')
for name in names:
    print(name )

for index , nam in enumerate(names,start=1):
    print(f'{index } the name is {nam}')
indexs=0
print('--------------------------------------------------------')
while indexs <  len(names ):

    print(f'{indexs +1}the name is {names[indexs]}')
    indexs+=1