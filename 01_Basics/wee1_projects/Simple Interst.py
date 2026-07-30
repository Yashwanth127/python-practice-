'''
Problem
Calculate simple interest given principal, rate, time.

Step 1: Understand
Input: P, R, T

Output: SI

Formula: SI = (P × R × T) / 100

Step 2: Write logic
Take P, R, T

Apply formula

Print SI
'''


principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)