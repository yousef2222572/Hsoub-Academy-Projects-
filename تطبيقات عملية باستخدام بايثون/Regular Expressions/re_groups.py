#groups
from re import *
text ='559-484-4389'
t=search(r'(\d{3})-(\d{3})-(\d{4})',text)
print(t.group(1))

print(t.group(2))
print(t.group(3))
print('------------------------------------------------------------------')
date= '23-12-2025'
dat=search(r'(\d{2})-(\d{2})-(\d{4})',date)


day=dat.group(1)
month=dat.group(2)
year=dat.group(3)
print(f'the day is {day} the month is {month} the year is {year}')
print(dat.group())
print(dat.groups())
