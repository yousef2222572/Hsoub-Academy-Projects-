from pathlib import Path
import csv

with open(Path.home()/Path('Desktop','yousef','programing','hsoub_academy','تطبيقات عملية باستخدام بايثون','json_andcsv.py','names.csv'),'w')as file:
    write_d=csv.DictWriter(file,['Name','salary','ages'])

    write_d.writeheader()
    write_d.writerow({'Name':'ali','salary':'2000','ages':'32'})

    