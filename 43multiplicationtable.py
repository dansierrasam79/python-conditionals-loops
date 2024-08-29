# multiplication table
table_num = int(input("Which times table do you want?: "))

for num in range(1,11):
    print(str(table_num),"X",str(num),"=",str(table_num*num) )
