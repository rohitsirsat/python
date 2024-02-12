n = int(input("Entere number : "))

even_sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
        
print("sum of even numbers : ", even_sum)