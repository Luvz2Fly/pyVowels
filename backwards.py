# Take an input and make it print out backwards

data = input("Type something here and I will print it backwards: ")
backwards = list(data)
backwardsOutput = ''.join(backwards[::-1])
print(backwardsOutput)

# Slim it down...
data = input("Type something here and I will print it backwards: ")
print(''.join(list(data)[::-1]))

