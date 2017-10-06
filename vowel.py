vowels = ['a', 'e', 'i', 'o', 'u']
word = "New Word Version 2"
for letter in word:
    if letter in word:
        if letter in vowels:
            print(letter)
