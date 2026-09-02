#map.  filter.   reduce
from functools import reduce

nums=[1,2,3,4,5,6,7]


def get_s(x):
    return x **2

squares=map(get_s,nums)
print(list(squares))


y=lambda x : x**2

square=map(y,nums)
#----------------------------------------

temps=[('ryahad',40),('amman',27),('dobi',32)]

def c_to_f(index_item):

    return   1.8*index_item[1]+32 , f'{index_item[0]}'
    return   
item=(map(c_to_f,temps))
print(list(item))

f_temps=[]
for i in temps:
    print(1.8*i[1]+32,i[1])
    
print('-------------------------------------------------------------------')
pepols=[('ahmad',2000),('smamer',2012),('yousef',2011),('mahmoud',1985)]
def old (the_item):
    return the_item[1]   < 2010

f=filter(old,pepols)
print(list(f))



print('-----------------------------------------------------------------------------------------------------------')



pepols=[('ahmad',2000),('smamer',2012),('yousef',2011),('mahmoud',1985)]


def find(itrabel,text):
    def finder (lang):
        for i in lang :
            if str(i).startswith(text):
                return True
            else :return False
    return list(filter(finder,itrabel))
c=find(pepols,input('inter the name'))           
print(c)





print('-------------------------------------------reduce---------------------------------------------------------------')








nums=[1,2,3,4,5,2,6]

def add(x,y):
    return x+y

print(reduce(add,nums))


print(sum(nums))


numss=[2,54,33,5,43,3,43,2]

maxs=reduce(lambda x,y : x if x > y else y ,numss)

print(maxs)

print(max(numss))













