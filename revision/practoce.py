#two find sqauare of the number
num1 =int(input("Enter the number 1 "))
print(num1*num1)

#odd or even
num1 =int(input("Enter the number 1 "))
if num1 % 2 ==0:
    print("its even ")
else:
    print("its odd ")


# to loops print number from 1 to n by user input
num1 = int(input("Enter the number in range "))
for i in range(1,num1 + 1):
    print(i)


# two add two number from funvtions
def add(a,b):
    return a+b
result=(add(5,20))
print(result)

#list arrays max number ugoising built in
num = [4, 8, 2, 10, 6]
print(max(num))

#without built in
num = [4, 8, 2, 10, 6]
larg = 0
for n in num:
    if n > larg:
        larg = n
print(larg)

#strings to find vowels
text = "education"
count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print(count)
