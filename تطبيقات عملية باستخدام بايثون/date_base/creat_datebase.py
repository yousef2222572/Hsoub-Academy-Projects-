import sqlite3
from pathlib import Path

sq_conect=sqlite3.connect(Path.home()/Path('Desktop','employees_1.db'))
print('all_good')
sq_run=sq_conect.cursor()


new_func="""CREATE TABLE if not exists users (
    sessionid ,
    chats ,
    chat ) """


sq_run.execute(new_func)

values="""INSERT INTO users VALUES ('123','learn_js,greating_chat','user=hello,model=hi who can i help you') """

sq_run.execute(values)

sq_conect.commit()





sq_conect.close()
