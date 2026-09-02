import sqlite3 
from pathlib import Path
import re
open_s=sqlite3.connect(Path.home()/Path('Desktop','employees_1.db'))

NEW_TABLE='''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    session_id TEXT)'''

cursor=open_s.cursor()

cursor.execute(NEW_TABLE)
id='550e8400-e29b-41d4-a716-446655440000'
def is_id(id):
    return bool(re.match(r'',id,))
cursor.execute('INSERT INTO user (session_id) VALUES (?)',(id,))
open_s.commit()

cursor.execute("SELECT session_id FROM user WHERE session_id= ?",(id,))
print(cursor.fetchone())




















