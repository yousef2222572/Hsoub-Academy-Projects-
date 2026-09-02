
from pathlib import Path
import os
print(os.getcwd())
my_list=['yousef','slman','sef','ahmad','mahmoud']
my_list='\n'.join(my_list)
#os.chdir(r'c:\Users\USER\Desktop')
#file_twp=open(r'yousef\programing\python acadmy with hasop\تطبيقات عملية باستخدام بايثون\file-Expressions\new_text.txt','r')
print(Path.home())
openfile=open(r'C:\Users\USER\Desktop\yousef\programing\python acadmy with hasop\تطبيقات عملية باستخدام بايثون\file-Expressions\new_text.txt','r')
with open(Path.home()/Path('desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions','new_text.txt'),'w') as new_file:
    new_file.write('hello how are you')
    new_file.writelines(my_list)




print(str(Path.home()/Path('desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions','new_text.txt')))