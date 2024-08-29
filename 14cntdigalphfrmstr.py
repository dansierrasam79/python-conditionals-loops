# count alph & digs from str
init_str = "Python 3.2"
count_dig, count_alph = 0,0
for char in init_str:
    if char.isalpha():
        count_alph += 1
    elif char.isdigit():
        count_dig += 1
print(count_dig,count_alph)