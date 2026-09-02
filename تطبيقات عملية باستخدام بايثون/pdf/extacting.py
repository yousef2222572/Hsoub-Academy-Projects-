import PyPDF2
import re
from pathlib import Path
pdf=open(Path.home()/Path('Desktop','Statement Att Safety and Environment Orientation Al Ajmi Employees -Hofuf 201-260','Statement Att Safety and Environment Orientation Al Ajmi Employees -Hofuf 2 [201].pdf'),'rb')
open_pdf=PyPDF2.PdfReader(pdf)
print(len(open_pdf.pages))
sheet1=open_pdf.pages[0]
input_text=sheet1.extract_text()
pattern = r"This is to certify that\s*(.*?)\s*Has participated in the following orientation"
    
match = re.search(pattern, input_text, re.DOTALL)

if match:
    print(match.group(1).strip())