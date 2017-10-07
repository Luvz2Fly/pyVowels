vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please provide a word with vowels! ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
                found.append(letter)
for vowel in found:
    print(vowels)
    print() #Test
print("PyCharm")
print("PyCharm and Git")
