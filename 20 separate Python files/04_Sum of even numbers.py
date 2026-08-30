n =int(input("Enter n: "))
total = 0
for i in range(2,n+1):
    if i%2==0:
        total = total=+i
    print("Sum of even numbers from 2 to", n, "is:", total)