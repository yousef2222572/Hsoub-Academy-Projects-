list_number=[1,2,3,4,5,6,7,8,9,10]
result=1
for i in list_number:
    result= i *result
print(result)
#-----------------------------------------
num = [5, 6, 7, 8, 0]
result = []
current_sum = 0

for i in num:
    current_sum += i
    result.append(current_sum)

print(result)

numb=[1,2,2,2,4,4,5,6,7,8,8]
dic=[]
sen=[]
n=0
for nu in numb:
    n+=1
    dic=[]
    if n==len(numb):
        if nu in dic:
            sen.append(nu)
print(sen)