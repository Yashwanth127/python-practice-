empname = input("Enter the Emp name: ")
sal = float(input("Enter the basic Salary: "))
service = float(input("Enter the Total years Service experience: "))

if service > 5:
    bonus = sal * 0.10
else:
    bonus = sal * 0.05

total_sal = sal + bonus

print("Employee Name:", empname)
print("Bonus:", bonus)
print("Total Salary:", total_sal)