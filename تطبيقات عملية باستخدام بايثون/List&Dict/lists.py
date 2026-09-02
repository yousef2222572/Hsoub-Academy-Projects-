

employees=['hasan','hadi','reem','ahmad']

print(employees)
print(employees[0])
print(employees[3])
print(employees[1])
print('--------------------------------------------------------------------')
print(employees[0:4])
print(employees[::2])

print(employees)

employees[0]='hamad'
print(employees)

employees[0:2] = 'hade' ,'salwa'
print(employees)

employees[1:]=''
print(employees)

print('-----------------------------------------------------------------------------')
#for loop 
employees=['hasan','hadi','reem','ahmad']
for i in range(4):
    print(employees[i])
for i in range(len(employees)):
    print(f'index is {i} , name {employees[i]}')


print('-----------------------------------------------------')
#enumerate

for index,item in enumerate(employees):
    print(f'index is {index+1} name is :{item}')

print('------------------------------------------------------------------------------------------------------')
#in and not in 
print('hasan' in employees )
'''
print('what employees name')
name=input()

if name not in employees:
    print('we have not '+name+' employees')
else:
    print(f'{name}is on as company')'''


import random 

print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))


random.shuffle(employees)
print(employees)


