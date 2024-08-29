# days of month
months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31,"August":31, "September":30, "October":31, "November":30, "December":31}
month_input = input("Enter a month: ")
for key, value in months.items():
    if key == month_input:
        print("No. of days: ", value)