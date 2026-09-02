import shutil
from os import rename
try :
    from pathlib import Path
    shutil.copytree(Path.home()/Path('Desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions'),Path.home()/Path('Desktop','yousef','the_new_folder'))
    shutil.copy(Path.home()/Path('Desktop','yousef','programing','python acadmy with hasop','تطبيقات عملية باستخدام بايثون','file-Expressions','project_file.txt'),Path.home()/Path('Desktop','yousef','the_new_file'))
    shutil.move(Path.home()/Path('Desktop','yousef','programing','telebord'),Path.home()/Path('Desktop','yousef'))
except :
    print('folder not found')

#shutil.move(Path.home()/Path('Desktop','yousef','programing','awosom.txt'),Path.home()/Path('Desktop','yousef','hello'))
shutil.move(Path.home()/Path('Desktop','yousef','programing','awosom.txt'),Path.home()/Path('Desktop','yousef','programing','the_one'))#to ching the namae

