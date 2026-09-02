with open('/Users/jousef/Desktop/ttth_file/text.text','a') as f, open('/Users/jousef/Desktop/ttth_file/textt.text','a') as f2:
    f.write('hello i am yousef')
    f.write('i am 14 year old')
    
    f2.write('hello i am yousef')
    f2.write('i am 14 year old')
    




with open('/Users/jousef/Desktop/ttth_file/text.text','r') as f:

    for line in f:
        print(line+'hell',end=' ',)




x=open('/Users/jousef/Desktop/ttth_file/five.png','r')

print(x.read())