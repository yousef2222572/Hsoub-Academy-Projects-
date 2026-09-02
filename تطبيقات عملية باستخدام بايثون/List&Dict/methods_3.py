hadi={
    'name':'hadi',
    'number':'0538283687',
    'skils':['python','css','javascript']

}

#print(hadi['name']+'get a salary'+str(hadi['salary']))
print(hadi['name']+'get a salary'+str(hadi.get('salary','no salary')))


print('---------------------------------------------------------------------------------')
#setdefault


print(hadi)
print(hadi.setdefault('salary',2000))
print(hadi)

#thats mean if the the key not in the dect append it to the dect

print('----------------------------------------------------------------------------------------------')
#update
numbers={1:'one',2:'three'}
print(numbers)
numbers.update({2:'two'})
print(numbers)
numbers.update({3:'three'})
print(numbers)

print('---------------------------------------')
#clear()
numbers.clear()
print(numbers)