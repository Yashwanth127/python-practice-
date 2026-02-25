#append
nu=[10,23,23]
nu.append(70)
print(nu)

#extend
num=[29,23,45,56]
num.extend([90,230,234])
print(num)

#remove
num.remove(23)
print(num)

# To remove TWO values (29 and 45)
to_remove=(29,45)
for val in to_remove:
    num.remove(val)
print("after the removing of numbers is ", num)