password = input("entere your password : ")

if len(password) <= 6:
    Strength = "weak password"
elif len(password) > 6 and len(password) <= 10:
    Strength = "medium password"
else:
    Strength = "STRONG PASSWORD"


print(Strength)