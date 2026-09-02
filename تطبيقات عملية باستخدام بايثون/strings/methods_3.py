#join

list_1=['hello','world']


print(',,'.join(list_1))

print('-'.join(list_1))
print('abc'.join(list_1))
print('----------------------------------------')

test='hello world'

print(test.split(' '))

test='helloabcworld'

print(test.split('abc'))

test='''hello
how are you
i am fine '''

print(test.split('\n'))

print(test.splitlines())

test='hello \n how are you\n i am fine\n'
print(test)
print(test.splitlines())