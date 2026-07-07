# Q1
#
# Take a number and print its square
num = int(input("Enter the number "))
square = num ** 2
print(square)

#Q2 Check whether a number is even or odd
num = int(input("Enter the number "))
if num % 2==0:
    print("even ")
else :
    print("odd ")


# Find the largest of 3 numbers
num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
num3 = int(input("Enter the number "))

largest =max (num1, num2, num3)
print("the largest number is ",(largest))

# Q4 Print numbers from 1 to 50
# only  tiples of 3
for num1 in range(1,50):
    if num1 % 3 ==0:
        print(num1)

# Q5 Find sum of digits of a number
num1 = int(input("Enter the numbers "))
total = 0
while num1 > 0:
    digit = num1 % 10
    total += digit
    num1 = num1 // 10
print(total)

#🔵 LOOPS + LOGIC heck whether a number is prime
# Check if number is prime
number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not prime")
elif number == 2:
    print("2 is prime")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")
