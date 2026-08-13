'''num = 7
for i in range (2, num):
    if num % i ==0:
        print("not a prime ")
        break
else:
    print("prime ")
    '''

num = int(input("Enter the number  "))
if num <=1:
    print("not a prime ")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime ")
            break
    else:
        print("Prime ")

for num in range(2,21):
    for i in range(2,num):
        if num %i == 0:
            break
    else:
        print(num)


