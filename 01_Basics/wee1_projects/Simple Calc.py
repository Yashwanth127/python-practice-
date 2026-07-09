num1 =int(input("Enter the number "))
num2 =int(input("Enter the number 2"))

add = num2+num1
mul =num2*num1
min=num2-num1
div=num2/num1 #ensure the num1 must not be zero


print(f"add : {add}")
print(f"mul : {mul}")
print(f"min : {min}")
print(f"div : {div}")

#operation choice
print("choose operation: +, -,*,/")
op = input("enter operation: ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)