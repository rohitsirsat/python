age = int(input("Entere your age :"))

if age < 13:
    print("children")
elif age < 20 and age > 13:
    print("teeandager")
elif age < 60 and age > 20:
    print("adult")
else:
    print("senior")


