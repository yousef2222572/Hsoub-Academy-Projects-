"""

def the_name(name):
    print(f'hello {name}')

the_name("yousef")


def names(name,age,weight=59):
    print(f'hello {name}',f'your age is {age}',weight)

names(name='yousef',age=13)
names(age=43,name='yousef')
"""
"""
def printfrots(*args):
    for frout in args:
        print(f'i love {frout}')

printfrots('yousef','ahmad')

"""
"""

def wether(**args):
    print(args)

wether(contry='span',wether='cool',peopole='happy')
"""

def nums():
    one_num=int(input('hello enter a one num'))
    two_num=int(input('hello enter a two num'))
    print(one_num ** two_num)
nums()

    