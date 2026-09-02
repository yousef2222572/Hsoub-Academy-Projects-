'''
def my_generator():
    i=0
    print('first value')
    yield i
    i += 1
    print('socond value')
    yield i
    i+= 1
    print('last value')
    yield i 

gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


def gen(n,a):
    i = 1
    print(f'your name is {n}')
    yield i
    i+=1
    print(f'your age is {a}') 
    yield i
    i+=1
g=gen('yousef',14)

print(next(g))
print(next(g))



def sernum (num):
    for i in range(1 , num , 2):
        yield i
se=sernum(100)
def ss (the_gen):
    for i in  the_gen:
        yield i ** 2



print(sum(ss(sernum(100))))

odds_nums=(i for i in range (1,10,2))


cr=(i **2 for i in odds_nums )
print(sum(cr))

'''

cr_odds=(num**2 for num in range(1,10,2))
print(sum(cr_odds))