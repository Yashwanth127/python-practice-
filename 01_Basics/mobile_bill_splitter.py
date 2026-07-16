rent = int(input("Enter the month rent  "))
DataUsed = int(input("Enter the Total Data used in GB   "))
Charge=int(input("Enter the price per one GB "))
total_call =int(input("Enter how many min of call "))
charge_permin=float(input("Enter the charge per min for a call "))
friends=int(input("Enter how many friends sharing the bill "))

Datacost= DataUsed * Charge
call_Cost = total_call * charge_permin
total_bill = rent + Datacost+call_Cost
Per_person_amount=total_bill / friends

print("======Bill Splitter=======")
print("\ntotal Datacost is ",Datacost)
print("\ntotal call_Cost ",call_Cost)
print("\ntotal bill ",total_bill)
print("\nper Person total amount is ",Per_person_amount)
print("=======sharing is caring Friends=========")