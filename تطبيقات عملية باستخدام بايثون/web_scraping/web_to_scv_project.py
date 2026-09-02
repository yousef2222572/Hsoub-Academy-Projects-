import requests
import bs4
from pathlib import Path
import csv
headers = {
    "User-Agent": "YousefWebScraper/1.0 (contact: yousef)"
}
response = requests.get(
    "https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers",
    headers=headers
)

# print(response.text)



soup=bs4.BeautifulSoup(response.text,'html.parser')


table_soup=soup.find_all('table')

filter_table=[table for table in table_soup if table.caption is not None  ]




required_table=None

for table in filter_table :
    if 'Top first languages by percentage per CIA' in str(table.caption.text.strip()) :
        required_table=table
        break
    
# print(required_table)

rows = required_table.find_all('tr')
# print(rows)

header_rows=[row.text for row in rows[0].find_all('th') ]

# print(header_rows)

data_body=[]
for row_b in rows :
    
    body_value=row_b.find_all('td')
    
    if len(body_value) == 0 :
        continue
    
    data_list=[bd.text.strip() for bd in body_value ]
    
    data_body.append(data_list)


csv_file=open(Path.home()/Path('Desktop','web_scrap_csv') ,'w',newline='')
    
    
writer=csv.writer(csv_file)

writer.writerow(header_rows)
writer.writerows(data_body)
    
    
