year = int(input("entere year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year")
else:
    print(year, "is NOT leap year")