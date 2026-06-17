#YYYY/MM/DD

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ")
    try:
        #MONTH/DAY/YEAR format
        if "/" in date:
            month, day, year = date.split("/") #splitting the date at "/"

            #converting to int
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31: #range of the months and the days
                print(f"{year}-{month:02}-{day:02}") #turning the months and days into a two digit var
                break

        #MONTH NAME/DAY/YEAR format
        elif "," in date:
            month, rest = date.split(" ", 1)
            day, year = rest.split(", ")

            #converting to int
            month = months.index(month) + 1 #as the index starts from zero
            day = int(day)
            year = int(year)


            if 1 <= month <= 12 and 1 <= day <= 31: #range of the months and the days
                print(f"{year}-{month:02}-{day:02}") #turning the months and days into a two digit var
                break

    except(ValueError, IndexError):
        continue

