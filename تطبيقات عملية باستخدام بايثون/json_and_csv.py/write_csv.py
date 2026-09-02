import csv
from pathlib import Path



'''
cv.close()

cv=open(Path.home()/Path('Desktop','names.csv'))
read=csv.reader(cv)



data=list(read)
print(data)
cv.close()



with open(Path.home()/Path('desktop','employees.csv'),'a',newline='') as emp:
    writer=csv.writer(emp)
    emplo=['ahmad','salem','salwa','qasem']
    salaryes=[1332,2313,6342,4313]
    data=[2025,2024,2021,2021]
    for i in range(len(salaryes)):
        writer.writerow([emplo[i],salaryes[i],data[i]])
        
'''

'''
header=[
    ['name','salary','date']
]
data=[
    ['haid', 3232,2021],
    ['salem',3221,2020],
    ['sara', 3232,2022]
]

value=csv.writer(cv)
value.writerows(header)
value.writerows(data)
cv.close()
'''

cv=open(Path.home()/Path('Desktop','names.csv'),'w+',newline='')
write=csv.writer(cv,delimiter='\t',lineterminator='\n------------------------\n')
write.writerow(['ahmad',2342,'2025'])
cv.close()
