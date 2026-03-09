text = input("Enter a string: ")
result = ""

for ch in text:
    if ch != " ":
        result = result + ch

print(result)