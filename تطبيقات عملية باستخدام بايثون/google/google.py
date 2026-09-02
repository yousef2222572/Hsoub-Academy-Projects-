import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes=[
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentiols=ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)
file=gspread.authorize(credentiols)


