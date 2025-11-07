num = int(input("Enter the number "))
orginal = num
rev = 0
while num >0 :
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if orginal == rev :
    print("it's a palindrome ")
else:
    print("its not a palindrome ")

