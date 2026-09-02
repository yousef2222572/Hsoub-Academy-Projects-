import csv 
from pathlib import Path

cv=open(Path.home()/Path('Desktop','names.csv'))
read=csv.reader(cv)
data=list(read)

for row in data :
    print('row' ,row[0],row)

for i in range(len(data[0])):
    print(data[0][i] ,end=' ')

