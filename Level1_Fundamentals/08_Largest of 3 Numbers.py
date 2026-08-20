a =int(input("Enter the number1 "))
b =int(input("Enter the number2 "))
c =int(input("Enter the number3 "))
if a==b==c:
    print("All numbers are equal ")
elif a>=b and a >= c:
    print("largest number is  ",a)
elif b>=a and b>=c:
    print("largest number is  ",b)
else:
    print("largest number is  ",c)

