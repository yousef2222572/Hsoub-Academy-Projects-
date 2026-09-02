'''class Schoole:
    def __init__(self,name,location,whight,heght,techer_database,studes_databases):
        self.name=name
        self.location=location
        self.whight=whight
        self.heght=heght
        self.techer=techer_database
        self.stude=studes_databases
    
    def info(self):
        return f'schoole name is {self.name} location schoole is {self.location} '
    def database (self,):
        which =input ('which one do you want techers base or studint base ')
        if which == 'studint base' :
            return f'this is your studint data base ({self.stude}) '
            
        if which== 'techers base':
            return f'this is your techers data base ({self.techer}) '
        else: return 'you dont write any thing '

    def append (self,the_appended):
        appe=int(input('if you want to append techer send 1 if you want to append studint send2'))
        if appe == 1:
            self.techer.append(the_appended) 
            return self.techer
        if appe == 2:
            self.stude.append(the_appended)
            return self.stude
        else:return 'you dont write any thing yet'
'''

class all:
    def __init__(self,name,age,birth_day):
        self.name=name
        self.age=age
        self.birth_day=birth_day
    def info (self):
        x=f'the name is {self.name} the old is {self.age},  the birth day is {self.birth_day}'
        return x
class techers(all):
    def __init__(self,id):
        super().__init__(name,age,birth_day)
        
class studint(all):
    def __ini__(self,id):
        super().__init__(self.name,age,birth_day)
        self.id=id

ahmad=techers(name='ahmad',age)
schoole=Schoole(name='future_schoole',location='dobi',whight=1000,heght=1000,techer_database=['ahmad','salm','sarah','hamza','alla',],studes_databases=['ahmad','salem','somaia','slwa','nora','hamad'])
print(schoole.info())
print(schoole.database())
print(schoole.append('ahmad'))/Users/jousef/Desktop/yousef/programing/python acadmy with hasop/اساسيات لغة بايثون