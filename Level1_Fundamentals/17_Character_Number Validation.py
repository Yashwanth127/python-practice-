char = input("Enter a character: ")

if char.isalpha():
    print(char, "is an alphabet")

elif char.isdigit():
    print(char, "is a number")

else:
    print(char, "is a special character")