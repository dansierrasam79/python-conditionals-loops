#get next day
thirty_one = ['01','03','05','07','08','10','12']
thirty = ['04','06','09','11']
twenty_eight = ['02']
twenty_nine = ['02']
year = int(input("Enter a year (1900-2024): "))
month = input("Enter a month (01-12): ")
dte = int(input("Enter a date (1-31): "))

#scenario 1: within the date of 1 to 30
if dte >= 1 and dte <= 29 and month not in twenty_nine and month not in twenty_eight:
    print("Next day: ", str(dte+1),"-",str(month),"-",str(year))
elif dte == 30 and month in thirty_one:
    print("Next day: ", str(dte+1),"-",str(month),"-",str(year))
# scenario 2: with date 30 and month in 30
elif dte == 30 and month in thirty:
    print("Next day: ", "01","-","0"+str(int(month)+1),"-",str(year))
# scenario 3: with date 31
elif dte == 31 and month in thirty_one:
    if month != "12":
        print("Next day: ", "01","-","0"+str(int(month)+1),"-",str(year))
    else:
        print("Next day: ", "01","-","01","-",str(int(year)+1))
#scenario 4: handling february, both leap and non-leap year
elif dte == 28 and month in twenty_eight:
    print("Next day: ", "01","-",str(int(month)+1),"-",str(year))
elif dte == 29 and month in twenty_nine:
    print("Next day: ", "01","-",str(int(month)+1),"-",str(year))
