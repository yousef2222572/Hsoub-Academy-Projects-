import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes=[
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentiols=ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)
file=gspread.authorize(credentiols)

x=file.open('new_one')

work_sheet=x.get_worksheet(0)
work_sheet.update_cell(10,1,'=sum(B2:B9)')
work_sheet.update_cell(10,2,'=MAX(B2:B9)')
work_sheet.update_cell(10,3,'=AVERAGE(B2:B9)')
work_sheet.update('e3',[['hello']])
print(work_sheet.cell(10,3,value_render_option='FORMULA'))
work_sheet.batch_clear(['A1'])