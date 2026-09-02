import re 


text='yousef'
search=re.search('[a,y]',text)
print(search)
print(search.span())
print(dir(search))
print('------------------------')
print(search.group())



test='call me at 324-643-2354 tomorrow. 123-163-8492'
phone_number=re.search('\d{3}-\d{3}-\d{4}',test)
x=phone_number.span()
print(x)
test=f'{test[0:x[0]]} 714 651 4952 {test[x[1]:-1]}'
print(test)
print(search.group())
print(phone_number.string)


print('------------------------------------------------------------------------------')
#findall
txt='334 421 5665 is my phone number and my frind phone number is 323 422 3560'

phone_numbers=re.findall('\d{3}\s\d{3}\s\d{3}',txt)
print(f'your phone number is {phone_numbers[0]} and your frind phone number is {phone_numbers[1]}')


find=re.findall(r'A',txt)
print(find)
x=[]

def check_phone_num(the_num):
    is_phone_num=re.findall(r'\d{3}\s\d{3}\s\d{4}(?!\d)',the_num)
    if is_phone_num:
        x.append(is_phone_num[0])
        print(x)
    else:
        print('sorry that\'s a wrong num ')

while True:
        

    f=input('hello enter your phone number')

    if f=='':
        break

    check_phone_num(f)