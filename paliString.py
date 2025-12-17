s= input("Enter the word to check palindrome or not ")
rev=""
for char in s:
    rev = char + rev
if s == rev:
    print("its a palindrome ")
else:
    print("its not a palindrome ")

