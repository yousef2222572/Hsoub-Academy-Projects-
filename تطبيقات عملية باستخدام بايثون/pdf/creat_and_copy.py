from PyPDF2 import PdfWriter as w
from pathlib import Path
import  PyPDF2







#creat 

the_pdf=PyPDF2.PdfWriter()
open_pdf=open(Path.home()/Path('Desktop','three_pdf.pdf'),'wb')

#copy

filell_copy_from=open(Path.home()/Path('Desktop','pdf_test.pdf'),'rb')

sheet1=PyPDF2.PdfReader(filell_copy_from)




for i in range(len(sheet1.pages)):
    copy=sheet1.pages[i]
    the_pdf.add_page(copy)



the_pdf.write(open_pdf)

filell_copy_from.close
open_pdf.close