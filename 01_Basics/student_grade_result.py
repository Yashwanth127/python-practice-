name = input("Enter the Student Name: ")
sub1 =(int(input("Enter the Marks in sub1: ")))
sub2 =(int(input("Enter the Marks in sub2: ")))
sub3 =(int(input("Enter the Marks in sub3: ")))

total_marks =sub1+sub2+sub3
avg=total_marks/3

if avg >= 75:
    print("Grade A")
elif avg >= 65:
    print("grade B")
elif avg >= 50:
    print("Grade C")
elif avg >= 35:
    print("Grade D")
else :
    print("Fail")

if avg >= 35 :
    print("Pass")
else:
    print("Fail")

