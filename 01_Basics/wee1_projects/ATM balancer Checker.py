# ATM Balance Checker

name = input("Enter customer name: ")
balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))

if withdraw_amount <= balance:
    remaining_balance = balance - withdraw_amount

    print("\n===== ATM RECEIPT =====")
    print("Customer Name:", name)
    print("Withdrawal Amount:", withdraw_amount)
    print("Remaining Balance:", remaining_balance)
else:
    print("\nInsufficient balance")