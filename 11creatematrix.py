# generate 2d list
import random
print("Enter number of row and columns")
lst = [0,1,2,3,4,5,6,7,8,9]
final_lst = []
rows = int(input("Rows: "))
cols = int(input("Columns: "))
for i in range(0,rows):
    init_lst = []
    for j in range(0,cols):
        init_lst.append(random.choice(lst))
    final_lst.append(init_lst)
print(final_lst)