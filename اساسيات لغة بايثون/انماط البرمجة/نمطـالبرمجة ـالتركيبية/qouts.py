from random import choice
qouts_qustion=[
    'hello what is your name',
    'hello how old are you ',
    'hello where are you from',
]

def get ():
    return '\n'.join(qouts_qustion)

def add (str_user):
    if isinstance(str_user,str):
        qouts_qustion.append(str_user)
        return choice(qouts_qustion)        
    else: return 'thats not fun write a string'

