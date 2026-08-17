text = "yashwanth"

frequency = {}

for character in text:
    if character == " ":
        continue

    if character in frequency:
        frequency[character] = frequency[character] + 1
    else:
        frequency[character] = 1

print(frequency)