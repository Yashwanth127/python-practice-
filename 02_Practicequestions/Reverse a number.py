num = (int(input("enter the number ")))
rev= 0
original =num

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num //10

print("reverse: ",rev)