phone_book = {
    "Rahul": 9876543210,
    "Anita": 9123456780
}

name = input("Enter name: ")

if name in phone_book:
    print("Number:", phone_book[name])
else:
    print("Not found")