import re
user=input('please enter your email')
search_email=re.search(r'([A-Za-z.,-]{1,}@((gmail)|(hsoub)|yahoo|mail)(.com|.net|.edu|))',user)
print(search_email)