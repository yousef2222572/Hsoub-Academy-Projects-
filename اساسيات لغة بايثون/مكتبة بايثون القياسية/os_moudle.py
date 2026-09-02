import os , shutil
print(os.getcwd())
os.chdir('/Users/jousef/Desktop/yousef/programing/python acadmy with hasop/اساسيات لغة بايثون/مكتبة بايثون القياسية')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
'''os.chdir('folder_two')'''
print(os.getcwd())
os.chdir('..')
print(os.listdir())
content=os.scandir()
for item in content:
    if not item.is_file():
        print(item.name)



h=os.scandir()

for i in h:
    if not i.is_file:
        print(f'{i.name} is a folder')

try:
    os.makedirs('hello.folder/welcome.folder')
except FileExistsError as erf:
    os.chdir('hello.folder')
    print(os.listdir())
    
    print(erf,'thats olrdy here')
print(os.getcwd())


os.chdir('..')
print(os.getcwd())
'''os.rmdir('folder1')'''


print(os.getcwd())
shutil.copy2('اساسيات لغة بايثون/مكتبة بايثون القياسية/text_one.txt','hello.folder/text_one.text')
shutil.move('اساسيات لغة بايثون/مكتبة بايثون القياسية/text_two.text','hello.folder/the_text.text')
