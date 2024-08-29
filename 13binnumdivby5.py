# binary values div by 5
bin_values = "0100,0011,1010,1001,1100,1001"
bin_lst = bin_values.split(",")
for bin in bin_lst:
    if int(bin, 2) % 5 == 0:
        print(bin)