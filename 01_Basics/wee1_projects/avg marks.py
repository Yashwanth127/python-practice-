# average_marks.py
# Calculates total and average marks of three subjects.

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3

print("\n--- Marks Summary ---")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Total marks:", total)
print("Average marks:", average)

# Simple pass/fail based on average
if average >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")