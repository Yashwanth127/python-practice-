#defining function and F name is greet
def greet(name):
    print(" hello Good morning", name)
greet("yashwanth")
greet("chithra")

#return value
def add(a,b):
    return a+b
print(add(5,6))

#Calling Function
def greet():
    print("Good afternoon ")
greet()

#using function to check weather the given nunnber is odd or even
def add_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(add_even(9))

#factorial number
def fact(num):
    fact =1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(fact(10))
