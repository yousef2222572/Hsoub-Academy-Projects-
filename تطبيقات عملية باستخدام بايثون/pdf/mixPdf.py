import PyPDF2 , os
from pathlib import Path 
files=os.listdir(Path.home()/Path('Desktop','will_mix'))
allowed_files_list=[]
for file in files:
    if file.endswith('.pdf'):
        allowed_files_list.append(file)

allowed_files_list.sort()
print(allowed_files_list)
mix_file=open(Path.home()/Path('Desktop','will_mix','mix_file'),'wb')
mix_sheets=PyPDF2.PdfWriter()
x=0
for file in allowed_files_list:
    x+=1
    
    file=open(Path.home()/Path('Desktop','will_mix',file),'rb')
    sheets=PyPDF2.PdfReader(file)
    
    for page_num in range(len(sheets.pages)):
        if x==1 or page_num >=1:
            mix_sheets.add_page(sheets.pages[page_num])


mix_sheets.write(mix_file)

mix_file.close
file.close