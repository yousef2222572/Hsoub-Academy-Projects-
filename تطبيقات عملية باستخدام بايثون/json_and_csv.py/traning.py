from pathlib import Path
import csv

with open(Path.home()/Path('Desktop','yousef','programing','hsoub_academy','تطبيقات عملية باستخدام بايثون','json_andcsv.py','names.csv'),'w')as file:
    write=csv.writer(file)
    header=write.writerow(['names','salaryes','age'])
    values=write.writerows([
        ['ahmad','salem','sara','hamza'],
        ['2000','3000','1560','10'],
        [29,39,28,23,33],
    ])
