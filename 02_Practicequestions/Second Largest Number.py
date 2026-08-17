numbers = [10, 25, 7, 42, 18, 35]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Largest number:", largest)
print("Second largest number:", second_largest)