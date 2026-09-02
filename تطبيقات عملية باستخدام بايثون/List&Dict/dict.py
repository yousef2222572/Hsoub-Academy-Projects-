'''names=['hadi','yara','hasan','sara','osama']

salary=[3842,3342,4534,3532,4532



]

'''

hadi={
    'name':'hadi',
    'salary':'20000',
    'number':'0538283687',
    'skils':['python','css','javascript']

}



print(hadi)

print(hadi['skils'][1])
print(hadi['salary'])


print('---------------------------------------------------------')

list1=['yousef','ahmad','salem']
list2=['ahmad','yousef','salem']
print(list1==list2)
print(list1 in list2)
print(list1[0])
print(list2[0])
print('------------------------------------------------')

dect={
    'name':'tone',
    'species':'cat',
    'age':'4'
}

dect2 ={
    'age':'4',
    'name':'tone',
    'species':'cat',
}


print(dect==dect2)

'''
birth_days={'ahmad':2000,'salem':1997,'mahmoud':1998}
while True:
    x=input('hello enter your frind name ')
    if x !='':
        if x in birth_days:
            print(f'your frind birth day on {birth_days[x]}')
        else:
            print(
            'this name is not in the frind list'
        )
            new_bd=input(f'\nare you want to add this frind to the list just append the birth day to {x} name')
            birth_days[x]=new_bd
    else:break
'''



hadi={
    'name':'hadi',
    'salary':'20000',
    'number':'0538283687',
    'skils':['python','css','javascript']

}

print(hadi.keys())
print(hadi.values())
print(hadi.items())


yousef={
    'front_end':{
        1:'html',
        2:'javascript',
        3:'css'
    },
    'back_end':{
        1:'python',
        2:'jva',
        3:'PHP'
    }
}

print(yousef)
print(yousef['back_end'])
print(yousef['back_end'][1])
print(yousef['front_end'])
print(yousef['front_end'][2])

