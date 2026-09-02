# first i should import the Libraries, 
# first library (os) its helps as to handlign the files 
import  os
# socend library (csv) its to can edit (read,write , delet ,so on) csv files
import csv
# third library (pathlib) its to can edit the path of files or folder fast
from pathlib import Path

# here how i use the os , path to import the csv file 

folder_name_input = input('are you ready to get your headers from your csv files just write the name of your folder but it should exsist in the desktop')



os.makedirs(Path.home() / Path('Desktop', folder_name_input), exist_ok=True)
# here i get the files name in a loop to pass in every file
for file_name in os.listdir(Path.home() / Path('Desktop', folder_name_input)):
    # here I check the file type Via the file extension
    if not file_name.endswith('.csv'):
        continue
        
    print('remove header form ' , file_name , '...')
    
    
    # here I make a list to put every header in it
    csvrow = []
    
    # here I use the file name that i get it from the first loop in file_name
    csvfile_obj = open(Path.home() / Path('Desktop', folder_name_input, file_name))
    
    # I read it here
    reader_object = csv.reader(csvfile_obj)
    
    # I check here the line_num to add it 
    for row in reader_object:
        if reader_object.line_num == 1:
            continue  
        csvrow.append(row)
        
        
    # I close it here 
    csvfile_obj.close()
    # I put it into the csvfile
    csvfile_obj = open(Path.home() / Path('Desktop', folder_name_input, file_name), 'w', newline='')
    csvWriter = csv.writer(csvfile_obj)
    for row in csvrow:
        csvWriter.writerow(row)
    print(csvrow)
    csvfile_obj.close()