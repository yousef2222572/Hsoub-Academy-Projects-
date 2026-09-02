import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes=[
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentiols=ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)
file=gspread.authorize(credentiols)


work_sheet=file.open_by_url('https://docs.google.com/spreadsheets/d/1BsHtxHFhWNWmKOkeEy5DT-ahExgPal2u80Q0u5ZMlY8/edit?usp=drive_link')
onesheet=work_sheet.get_worksheet


sheet1=onesheet(0)

#write
sheet1.update('C3',[['hello wrld']])
sheet1.update_cell(1,1,'hello world')

sheet1.update('A1:c3',[['ahmad','399','2020'],['salem','221','2020'],['salem','221','2020']])