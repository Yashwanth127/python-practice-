#sum of n numbers using math formula
n=int(input("Enter the number: "))
sum = n*(n+1)//2
print(sum)

# using for loop to sum of n numbers
n= int(input("Enter the number "))
sum=0
for n in range(1,n+1):
    sum=sum+n
print(sum)

#sum of array integers
arr = [1,23,44,56]
sum = 0
for i in arr:
    sum = sum+i
print(sum)

#built in fun program for sum of arr
arr = [1,23,44,56]
print(sum(arr))