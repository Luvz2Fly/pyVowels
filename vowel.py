vowels = ['a', 'e', 'i', 'o', 'u']
word = "New Word Version 2"
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
                found.append(letter)
for vowel in found:
    print(vowel)
