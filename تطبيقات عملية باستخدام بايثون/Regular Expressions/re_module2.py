import re

#sub

string='helllo my phone number is 334-224-6535 and my frind phone number is 233-221-4443'

replace=re.sub(r'\d{3}-\d{3}-\d{4}','333 333 3333',string)
print(replace)

fact='5,3,5factorial()'
replace=re.sub(r'(?<=,)\dfactorial\(\)','*factorial(5)',fact,1)
print(replace)

sentens='i am student at hsop academy'
replace=re.sub(r'\s','-',sentens)
print(replace)


print('-------------------------------------')
#split
txt='i am student at hsoub acdemy'
search=re.split(r'\s',txt,3)
print(search)

replace=re.sub(r'\s','-',txt)
print(replace)

sp=re.split(r'-',replace)

print(sp)



test='restart-uplod-the-files-after-lose-connect-in-javascript'

replace=re.sub(r'-',' ',test)
print(replace)
test='restart-uplod-the-files-after-lose-connect-in-javascript'


sp=re.split(r'-',test)
d=['2','f']
x=' '.join(sp)
print(x)

