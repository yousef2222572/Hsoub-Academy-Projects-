'''
print(4+4)
print('hello'+'world')
name='yousef'
nums=[1,2,3,4,5,6,4]
print(len(name))
print(len(nums))
--------------------------------------------------
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        return point(self.x+ other.x , self.y+other.y ,self.z+other.z)
    def __str__(self):
        return f'{self.x},{self.y},{self.z}'



pt1=point(3,5,6)
pt2=point(2,6,3)
pt3=pt1+pt2
print(pt3)

class cart:
    def __init__(self,items):
        self.items=items

    def __getitem__(self,key):
        return self.items[key]

order1=cart(['pen','pencil','notebook'])
print(order1.items[0])
print(order1[0])

'''


class point: