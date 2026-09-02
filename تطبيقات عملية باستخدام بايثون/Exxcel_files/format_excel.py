import openpyxl
from pathlib import Path

excel_file=openpyxl.load_workbook(Path.home()/Path('Desktop','emplyees.xlsx'))
sheet_one=excel_file['Sheet1']
sheet_one['c9']='=(sum(c2:c8))'
sheet_one['c9']='=(average(c2:c8))'
sheet_one['c10']='=countif(c2:c8,">5000")'
del sheet_one['b9']
excel_file.save(filename=Path.home()/Path('Desktop','emplyees.xlsx'))