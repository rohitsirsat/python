input_str = input("enter string : ")

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("and ans is : ", char)