num= [13,64,67,35,876,56,34,943,68,46,4]
my_num=[]
for i in num:
    if i > 30 :
        my_num.append(i)
print(my_num)
the_num=[i for i in num if i > 30]
print(the_num)
squares=[i**2 for i in range(11)]
print(squares)
n_squares=[]
for i in range(11):
    n_squares.append(i**2)
print(n_squares)
numbers=[14,56,345,6,864,32,5,75,74,84,843,36,84,967,]
num_100=[i if i <100 else 100 for i in numbers]
print(num_100)

dict={i:i**2 for i in range(10)}
print(dict)
numb=[1,2,3,4,5,6,7,7,7,8,8,9]
thenumbers={i for i in numb if i >2}
print('------------------------------------------------------')
print(thenumbers)
matrix=[[i for i in range(5)] for n in range(5)]
print(matrix)