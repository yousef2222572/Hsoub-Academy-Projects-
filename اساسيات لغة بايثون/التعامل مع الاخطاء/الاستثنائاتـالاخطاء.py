'''raise Exception('hello ')


try:
    with open('/Users/jousef/Desktop/ttth_file/text.text','a')as f:
        x=3
        y=9
        x=x/y
        f.write(str(x))


except ZeroDivisionError as zero :

    print(f'erooor the error is {zero}')

except FileNotFoundError as ree : 
    print(ree)
else:
    
    print( ' we are finsh and send to the file')
finally:
    print('its havent wrong')
'''

class toyoungerror(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
    

class toolderror(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return self.message


def old():
    old=int(input('how old are you'))
    if old <15 :raise toyoungerror('you are under 15')
    if old >45 :raise toolderror('you are up to 45')


try:
    old()
except toyoungerror as ty:
    print(ty)
except toolderror as ro :
    print(ro)