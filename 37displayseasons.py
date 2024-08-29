# Display season
seasons = {"Summer":["March", "April", "May", "June"], "Monsoon":["July","August","September"], "Autumn":["October","November"], "Winter":["December","January","February"]}
month = input("Enter the month: ")

for key, value in seasons.items():
    if month in value:
        print("Season: ", key)
