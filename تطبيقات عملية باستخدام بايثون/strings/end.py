print('enter a sintens ')
tow_words=[]
the_words=input()

the_words.lower()

the_words=the_words.split(' ')

x=len(the_words)


for i in range(x):

    tow_words.append(f'{the_words[-1]}')
    the_words.pop()

tow_words=' '.join(tow_words)

print(tow_words)

#revers