from pathlib import Path
import csv

with open(Path.home()/Path('Desktop','yousef','programing','hsoub_academy','تطبيقات عملية باستخدام بايثون','json_andcsv.py','names.csv'))as file:
    read=csv.DictReader(file)
    for row in read:
        print(row['names'],row['salaryes'],row['age'])

        