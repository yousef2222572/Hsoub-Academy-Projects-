class Prodect:
    def __init__(self,id,price,name,count):
        self.count=count
        self.id=id
        self.name=name
        self._price=price


    def des(self):
        self._price=self._price - 10

    def info(self):
        return f'id = {self.id}  name. {self.name} price {self._price} '
    

    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return str(self.__price)+'$'


    
'''
iphon_13=Prodect(id=1,name='iphon_13',price=30)
samsong_s22=Prodect(id=2 , name='samsong_s22',price=30)

print(iphon_13.price)
print(iphon_13.des())
print(iphon_13.price)

print(samsong_s22.info())


iphon_13=Prodect(id=1 ,price=999,name='iphon_13')


iphon_13.__price=0

print(iphon_13.get_price())

iphon_13._Prodect__price=0
print(iphon_13.info())
'''

class mobile(Prodect):
    def __init__(self,name,price,memory,id,count,storage,screen_size):
        super().__init__(name,price,count,id)
        self.memory=memory
        self.count=count
        self.storage=storage
        self.screen=screen_size

         

class lap(Prodect):
    def __init__(self,name,price,memory,id,count,storage,screen_size,keybaurd_size):
        super().__init__(name,id,price,count)


        self.memory=memory

        self.storage=storage
        self.screen=screen_size

        

iphon_17=mobile(price=999,name='iphon_17',id=5,count=23,memory=8,storage=778,screen_size=7.5)

print(iphon_17.info())