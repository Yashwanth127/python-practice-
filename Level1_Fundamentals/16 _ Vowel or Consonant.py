word = input("Enter a word: ")

for char in word:
    if char.lower() in "aeiou":
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")