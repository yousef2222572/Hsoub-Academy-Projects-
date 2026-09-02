class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return f'the x is {self.x} the y is {self.y} the z is {self.z}'
    def __add__(self,other):
        return self.x+other.x ,self.y+other.y, self.z +other.z
    
    def __lt__(self,other):
        x=self.y+self.x+self.z
        y=other.y+other.x+other.z
        return  x>y 
    def __gt__(self,other):
        x=self.y+self.x+self.z
        y=other.y+other.x+other.z
        return  x<y 

    


point_one=Point(5,7,11)
point_two=Point(3,6,2)
print(point_two)
print(point_one>point_two)
print(point_one<point_two)

