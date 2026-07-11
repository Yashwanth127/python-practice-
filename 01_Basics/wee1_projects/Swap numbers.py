# swap_numbers.py
# Swaps the values of two numbers.

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swap: a = {a}, b = {b}")

# Method 1: Using temporary variable
temp = a
a = b
b = temp

print(f"After swap (using temp): a = {a}, b = {b}")

# Method 2: Python shortcut
# a, b = b, a
# print(f"After swap (Python shortcut): a = {a}, b = {b}")