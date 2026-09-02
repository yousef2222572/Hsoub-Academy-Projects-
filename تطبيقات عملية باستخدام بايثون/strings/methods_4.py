#rjust , lfust, center

test='hello'
print(test.ljust(10))
print(test.rjust(10))
print(test.center(100))


print(test.rjust(11,'-'))
print(test.center(11,'-'))

print(test.ljust(11,'-'))

print('------------------------------------')

#expandtabs

test='hello\ti\tam\tyousef\t'
print(test)
print(test.expandtabs(41))