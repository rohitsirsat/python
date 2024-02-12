num = int(input("Entere your number : "))

for i in range(1, 11):
    if i == 5:
        continue
    print(i*num)