num={1,2,3,4,5,6,7,8,9}
print(type(num))
empty={}
empty=set(empty)
print(1 in num)
print(1 not in num)
print(len(num))

set1={1,2,3,4,5,5,5}
set2={6,7,7,8,9,3,9}
set3={10,11,11,12,13,14,15}
print(set1|set2|set3)
print(set1.union(set2,set3))
print(set1 & set2)
print(set2 - set1)
print(set1.difference(set2))
print(set1^set2)
print(set1|set2)
x=set()
print(x.add('hello'))
print(x)
print(type(x))
#print(x.remove('hello'))
#print(x.discard('e'))
print(x)
print(x.pop())
print(x)