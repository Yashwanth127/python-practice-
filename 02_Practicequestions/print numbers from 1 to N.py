def print_number(n:int)->None:
    if n<=0:
        return
    for i in range(1,n+1):
        print(i, end="  ")
        print()

print_number(20)

#Dry run
def print_numbers(n):
    if n<=5:
        return
    for i in range(1,n+1):
        print(i, end ="")
        print()

print_numbers(6)
