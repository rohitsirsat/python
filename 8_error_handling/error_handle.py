# ways to deal with file

# way 1
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()


# way 2 better way
with ('manager_txt', 'w') as file:
    file.write("better way")