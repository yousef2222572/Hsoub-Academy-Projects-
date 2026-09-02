import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
scopes=[
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentiols=ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)
file=gspread.authorize(credentiols)


worksheet=file.open('new_one')
worksheet=worksheet.get_worksheet(0)
names={'hadi':['3993','2000'],'sara':['3993','2000'],'yara':['3993','2000'],'ahmad':['3993','2000'],'reem':['3993','2000'],'anas':['3993','2000'],'mahmoud':['3993','2000']}

x=0
for key ,item in names.items():
    x+=1
    if x==1:
        worksheet.update_cell(1,1,'name')
        worksheet.update_cell(1,2,'salary')
        worksheet.update_cell(1,3,'date')
        worksheet.update_cell(9,1,key)
        worksheet.update_cell(9,2,int(item[0])+x*89)
        worksheet.update_cell(9,3,int(item[1])+x+10)
        x+=1
    worksheet.update_cell(x,1,key)
    worksheet.update_cell(x,2,int(item[0])+x*89)
    worksheet.update_cell(x,3,int(item[1])+x+10)

#search
cell=worksheet.find('hadi')
cell_all=worksheet.findall('hadi')
print(f'we have {len(cell_all)} two is have a column {cell_all[1].col} and row ({cell_all[1].row})')

print(f'we fount ({cell.value}) at the row is ({cell.row}) the column ({cell.col}) or ({cell.address})')

employees=re.compile(r'mahmoud|yara')
result=worksheet.findall('mahmoud')
print(result)

worksheet.update_cell(10,2,'=sup')