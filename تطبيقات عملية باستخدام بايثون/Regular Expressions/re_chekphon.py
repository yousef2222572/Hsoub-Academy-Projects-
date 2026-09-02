import re 

def check_phone(the_num):
    is_phone=re.search('\d{3}\s\d{3}\s\d{4}(?!\d)',the_num)
    if is_phone:
        print(f'{the_num} is append to the database')
        

x=str(input('enter your phone numbers'))

check_phone(x)
