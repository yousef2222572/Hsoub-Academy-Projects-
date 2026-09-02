import sqlite3
import csv
from pathlib import Path 

open_sq=sqlite3.connect(Path.home()/Path('Desktop','employees_1.db'))
cursor=open_sq.cursor()

new_table="""CREATE TABLE if not exists employess (
    id INTEGR  PRIMARY KEY,
    name VARCHAR(20),
    salary INTEGR,
    date TEXT
    )"""
    
cursor.execute(new_table)
print('all_good')

read_file=open(Path.home()/Path('Desktop','employees.csv'))
read_csv=csv.reader(read_file)




cursor.executemany("INSERT OR REPLACE INTO employess VALUES (? ,? ,? ,?)",read_csv)



open_sq.commit()
open_sq.close()
