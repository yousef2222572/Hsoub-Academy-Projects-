import random
words=['lion','table','door','bear','sun','deask',]
name=input("input your name for play a butfull game")
name=name.lower()
Approval=input(f'hello {name} i will chose now a word \n and you giv me a one later if you rady say (yes) if not (no)')
Approval=Approval.lower()


word=random.choice(words)

print('the name is ')
gusess=''

lives=12

while lives>0:
    failed=0

    for char in word:

        if char in gusess:
            print(char)
        
        else:
            print('-')
            failed += 1
        
    if failed==0:
        print('YOU WIN')
        print(f'the name is ',word)
        break
    guess=input('enter a liter')
    gusess+=guess
    if guess not in word:
        lives-=1
        print('roung answer') 
        print('you have a',lives, 'more')
        if lives == 0:
            print('you loss')