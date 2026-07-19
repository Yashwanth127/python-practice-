# Employee bonus calculator

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
years_of_service = int(input("Enter years of service: "))

if years_of_service >= 5:
    bonus = basic_salary * 0.10
else:
    bonus = basic_salary * 0.05

total_salary = basic_salary + bonus

print("\n====== Employee Salary Details ======")
print("Name:", name)
print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Total Salary:", total_salary)