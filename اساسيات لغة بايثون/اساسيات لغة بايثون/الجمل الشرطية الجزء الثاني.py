mynum=5
hisnum=int(input('hello inter a number'))
if hisnum != '':
    if hisnum > 0 :
        if hisnum==mynum :
            print('you wiiiiin')
        elif hisnum==mynum +1 or hisnum==mynum -1 :print('sooo close')
        else:print('you lose')
        if hisnum >10 :print('soo far')
    else:
        print('oh no this under the zero')
else:
    print('why you dont write any num')


#yousef=False
#if not yousef :
#    print('you are not yousef')

a=10
b=20
if a<b :
    min=a
else:
    min=b

min=a if a>b else  b
print(min)