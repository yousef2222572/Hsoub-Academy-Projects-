list=['yousef','ahmad','ayman']
print(list)
list1=[1,2,3,4]
list2=[2,1,4,3]
print([list1==list2])


list1=[1,2,3,4]
list2=[2,1,4,3,list1]
mylist=[False,23,'hello',]
print(mylist)
divises=['lap','phon','computer']
print(divises[0])
print(divises[1])

print(divises[-2])
print(divises[-1])

divises1=['smart tv','old tv','key bourd','mouse',[1,2,3,4,5]]
print(divises1[1][0])
print(divises1[1][1])

divises[0]= 'hello world'
print(divises)

del divises1[2]
print(divises1)

divises1 += ['smart bad','smart watch']
print(divises1)
divises1+=['note']
print(divises1)
divises1.append ('book')
print(divises1)
divises1.append(['hello world','hello user'])
print(divises1)
del divises1[-1]
divises1.extend(['hello world','hello user'])
print(divises1)
divises1.insert(0,'hello www.com')
print(divises1)
divises1.remove('hello world')
print('-------------------------------------------')
divises1.pop(0)
print(divises1)
print('hello user'in divises1)
divises1.pop(3)
print(divises1)
divises1.sort()#num or laters
print(divises1)
