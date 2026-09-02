from abc import ABC , abstractmethod

class shap(ABC):
    @abstractmethod
    def area(self):
        pass

    def info (self):
        return 'hello its the info'
    


class square(shap):
    def __init__(self,width,lenght):
        self.width=width
        self.length=lenght
    def area (self):
        return self.width * self.length 

class tringle(shap):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return self.base /2 * self.height
    


x=square(width=5,lenght=5)
print(x.area())
trangol=tringle(base=5,height=5)
print(trangol.area())
print(trangol.info())