number = int(input("entere number : "))
# number = 5

factorial = 1


while number > 0:
    factorial *= number
    # factorial = factorial * number
    number -= 1
    # number = number -1

print("factorial value is", factorial)
# output => 5*4*3*2*1 = 120


