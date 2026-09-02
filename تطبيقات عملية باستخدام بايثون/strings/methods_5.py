#index (substring,start,end)
test='hello world'

try:

    
    print(test.index('w',0,2))
except ValueError as val:

    print(val,'you are in wrong')

print('--------------------------------------------------------------------')
print(test.find('world'))
print(test.find('world',0,7))
print('--------------------------------------------------------------------')

#replace (old value , new value cou, count)

text='one plus one equal two'
text=text.replace('one','two')

if text == 'two plus two equal two':
    text='two plus two equal four'
    
    

print(text)