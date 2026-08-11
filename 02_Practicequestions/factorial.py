num =int(input("Enter the number: "))
if num<0:
    print("Factorial is not defined for Negative numbers ")
else:
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    print("factorial = ",fact)