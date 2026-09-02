'''
hisnum=int(input('hello enter a number'))

if hisnum >100 or hisnum <0 : 
    print ('what!! . this is a wrong number') 
    exit()
if 100 > hisnum > 90:
    print('your type number is from A')

if 89 > hisnum > 80:
    print('your type number is from B')

if 79 > hisnum > 70:
    print('your type number is from C')

if 69 > hisnum > 60:
    print('your type number is from D')

if 59 > hisnum > 50:
    print('your type number is from E')

if 49 > hisnum > 40:
    print('your type number is from F')

if hisnum in range(90,101):

    print ('your num is from A type')

while True:
    if hisnum in range(90,100):
        print('helo guest your num is from A type')
        break

while True:
    name=(input('hello what is your name '))
    if name == 'stop':
        print ('as you want')
        break
    else:
        birth_year=int(input(f'hello {name} but what is your birth year because i want to give you your old '))
        if  2024> birth_year > 0   :
            old=2024-birth_year
            print(f'oky are you ready..... your old is {old} ')
            break
        else:
            print ('are you kiding')
'''
'''
for y in range(1,5):
    print(y*x)
'''
x='*'

for i in range(0,5):
    print(5*x)
    if i == 2 :
        print('* pyton2 *')      
        continue
num=1
for i in range(1,5):
    for j in range(i +1):
        print(num , end=' ')
        num+=1
    print(' ')