# Take an input and make it print out backwards

def loop():
    # data = input("Type something here and I will print it backwards: ")
    # backwards = list(data)
    # backwardsOutput = ''.join(backwards[::-1])
    # print(backwardsOutput)

    # Slim it down...
    data = input("Type something here and I will print it backwards: ")
    print(''.join(list(data)[::-1]))
    ask()

def ask():
    again = input("Do you want to play again? (y/n)")
    if again.lower() == "y":
        loop()
    #while True:
    else:
        print("Thanks for playing")

loop()



