#check or even
def check_even(number):
    if number%2==0:
        print("even")
    else:
        print("odd")
check_even(4)
check_even(9)

#find_max
def find_max(a,b):
    if a>b:
        print(a)
    elif a==b:
        print("both are equal")
    else:
        print(b)
find_max(25,10)
find_max(7,7)