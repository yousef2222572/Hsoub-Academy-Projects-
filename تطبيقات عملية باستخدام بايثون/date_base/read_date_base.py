import sqlite3
from pathlib import Path 
open_sq=sqlite3.connect(Path.home()/Path('Desktop','employees_1.db'))
cursor=open_sq.cursor()
print('all good')


cursor.execute("SELECT id,name,salary FROM employess where salary >5000")
#print(cursor.fetchall())
#print(cursor.fetchone())
#print(cursor.fetchmany(6))
for i in cursor.fetchall() :
    print(i) 
