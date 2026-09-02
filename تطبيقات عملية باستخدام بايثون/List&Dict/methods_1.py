employees=['hasan','hadi','reem','ahmad']
employees.append('yara')
print(employees)
employees.insert(0,'mahmoud')
print(employees)


oldemployees=['osama','alaa']
employees.append(oldemployees)
print(employees)
print(oldemployees)
print(employees[6])
print(employees[6][1])

print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
employees=['hasan','hadi','reem','ahmad']
oldemployees=['osama','alaa']

employees.extend(oldemployees)
print(employees)


print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
#remove
employees.remove('alaa')
print(employees)

try:
    employees.remove('yosyef')
except ValueError as  ve:

    print(f' ohh no the error is {ve} put a right value')

employees=['hasan','hadi','hasan','reem','ahmad']
print(employees)

employees.remove('hasan')
print(employees)

print('-----------------------------------------')
#del statement
del employees[0]
print(employees)


print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#sort
nums=[3,34,6,6,2,6,8,4,22,34,66,3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)




employees=['hasan','hadi','reem','ahmad']
employees.sort()


print(employees)

employees.sort(reverse=True)
print(employees)

"""
spam=[2,5,2,3,6,'alice','bop']
spam.sort()
print(spam)"""



print('------------------------------------------------------')
#revers

employees.reverse()
print(employees)