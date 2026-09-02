import random
names=['yousef','ali','salem','mahmoud','abdalrahman','ahmad','hamza','omar','kaled']
the_choice_name=random.choice(names)
latter_use=input('hello are you redy to start as game you can put a one later or all the name \'yes\' or \'no\'  ')
latter_use.lower()
word=''
if latter_use=='yes':

    x=0
    tf=False
    while True:
    
        
        latter_user=input(f'rite a latter or a name its from  {len(the_choice_name)} lattr\n')
        if latter_user not in word :
            word+=latter_user
        

        if the_choice_name==(word):
            print('you win') 
            break
        if the_choice_name.startswith(word):
            tf=True
            y=len(the_choice_name)

            z=word+'-'*y
            f=z[:-len(word)]
            print(f)
        else:
            word=word[0:-1]
            x+=1
            print(word)
            if tf:
                print(f)
            print(f'you are have a {12-x} try')
            
            if x == 12 :
                print('you are lose')
                break

        





else:
    print('whay you dont want to play as game')
