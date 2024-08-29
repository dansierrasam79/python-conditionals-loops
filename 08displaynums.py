# display 0-9 except 3 & 6
lst = [num for num in range(0,7)]
for num in lst:
    if num == 3 or num == 6:
        continue;
    else:
        print(num, end = " ")