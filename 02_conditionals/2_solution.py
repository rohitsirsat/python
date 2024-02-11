age = int(input("enter your age : "))

day = input("entere day : ")



price = 12 if age >= 18 else 8
# print("ticket price is : $",price)

# if day == "Wednesday":
#     print("ticket price is : $", price-2)


if age >= 18:
    if day.lower() == "wednesdy":
        print("after discount : ",price-2)
    else:
        print("ticket price is : ",price)
elif age < 18:
    if day.lower() == "wednesdy":
        print("after discount : ",price-2)
    else:
        print("ticket price is : ",price)

