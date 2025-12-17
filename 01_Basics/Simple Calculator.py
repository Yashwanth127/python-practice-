a = int(input("Enter the number 1 " ))
b = int(input("Enter the number 2 "))
print("choose which Operation you need ")
print("1. Addition")
print("2. Multiplication")
print("3. Substraction")
print("4. Divison")
choose =int (input("Choose operation (1 - 4) "))
if choose == 1:
    print("Result ", a+b)
elif choose == 2 :
    print("Result ", a * b)
elif choose == 3:
    print("Result ",a-b)
elif choose == 4:
    if a&b!=0:
        print("Result ", a/b)
    else:
        print("the 0 cant be divided ")
else :
    print("The wrong operation you are selected ")