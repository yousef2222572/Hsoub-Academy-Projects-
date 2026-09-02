import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes=[
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentiols=ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)
file=gspread.authorize(credentiols)



#sheet_one=file.open('employees').sheet1
sheet_one=file.open_by_url('https://docs.google.com/spreadsheets/d/1hvzcaHXKhwt04NiCvfSdLIoRohhTrFmcwgwGSm3BftY/edit?usp=drive_link')
#sheet_one.sheet1.update_cell(1,1,'hello_world')
#worksheet=sheet_one.get_worksheet(0)
worksheet=sheet_one.worksheet('Sheet1')
worksheet_list=sheet_one.worksheets()
manager=['khaled','salman','mohamad','abd alrahman']
salary_list=['12000','15000','23000','29000']
'''
for l in range(1,4):
    if l==1:

        for i in range(1,len(manager)+1):
            worksheet.update_cell(i,1,manager[i-1])
            print('done')

    if l==2 :        
        for i in range (1,len(salary_list)+1):
            worksheet=sheet_one.worksheet('Sheet1')
            worksheet.update_cell(i,2,salary_list[i-1]+'$')
            print('done')
'''
#read my sheet

val=worksheet.acell('A2').value
print(val)


val=worksheet.cell(1,2).value
print(val)

values=worksheet.row_values(1)
print(values)


values=worksheet.col_values(1)
print(values)


list_of_lists=worksheet.get_all_values()
print(list_of_lists)


