from pathlib import Path

my_list=['yousef','mahamoud','salem','slman']



with open (Path.home()/Path('Desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions','project_file.txt'),'a')as new_file:
    new_file.writelines(my_list)

with open (Path.home()/Path('Desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions','project_file.txt'),'a')as new_file:
    new_file.writelines(my_list)
    new_file.write('hello how are you\n')
    new_file.write('hello how are you\n')
    new_file.write('hello how are you\n')
    new_file.write('hello how are you\n')
    new_file.write('hello how are you\n')