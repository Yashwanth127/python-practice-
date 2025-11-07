num= int(input("enter the  num "))
count = 0
print("Prime numers bw 2 and ", num, "are :")
for n in range(2 , num+1):
    for i in range(2, n):
        if n % i ==0:
            break
    else :
        print(n, end =" ")
        count += 1
print("\nthe number of prime number are ", count)

