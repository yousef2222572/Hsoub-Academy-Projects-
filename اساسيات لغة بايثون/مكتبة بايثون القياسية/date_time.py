from datetime import datetime
'''
my_birth_day=date(2005,11,4)
print(my_birth_day)

today=date.today()

print(today)

the_one=date.fromordinal(33933)

print(the_one)
from_ise=date.fromisoformat('2025-11-12')
print(from_ise)


my_birth_day=  today- my_birth_day
print(my_birth_day)

print(type(my_birth_day))

print(today > my_birth_day)
print(my_birth_day)
print(my_birth_day.isoformat())



#-------------------------time--------------------------------------------

time1=time()


print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)

time2=time(hour=4,minute=42,second=32)
print(time2.hour)
time3=time.fromisoformat('02:43:08')
print(time3)

'''
#------------------------------------datetime-------------------------------------
'''

word_cup_2032=datetime(year=2032 , month=11 ,day=1,hour=13, minute=00, second=0 )

print(word_cup_2032)

now=datetime.now()
print(now)
today=datetime.today()
print(today)


word_cup_2032=datetime.fromisoformat('2025-09-19 05:31:11')


print(word_cup_2032)


count=word_cup_2032-now
print(count)
'''










from datetime import timedelta,datetime





dati = timedelta(days=5, hours=12, minutes=23, weeks=2)

now=datetime.now()
print(now - dati)


date=datetime(year=2001,month=11,day=1)
date=datetime.strftime('%y/%m/%d')
print(date)