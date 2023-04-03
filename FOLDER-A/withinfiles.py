with open('with.txt', 'w') as file:
    file.write('hello world !')

f = open("with.txt", "r")
print(f.read())