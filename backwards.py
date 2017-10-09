# Take an input and make it print out backwards

data = input("Type something here and I will print it backwards: ")
backwards = list(data)
backout = ''.join(backwards[::-1])
print(backout)