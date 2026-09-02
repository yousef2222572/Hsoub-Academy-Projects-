import sqlite3
import openpyxl
from pathlib import Path
open_exel=openpyxl.Workbook()
sheet_1=open_exel['Sheet']
db=sqlite3.connect(Path.home()/Path('Desktop','employees_1.db'))

corser=db.cursor()



corser.execute("SELECT id,name,salary,date FROM employess")
s=0
for i in corser.fetchall() :
    s+=1
    for x in range(4):        
        lx=i[x]
        sheet_1.cell(s,x+1,lx)
















































open_exel.save(Path.home()/Path('Desktop','students_1.xlsx'))