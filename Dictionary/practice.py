#Basic Syntax
my_dict = {
    "key1": "value1",
    "key2": "value2"
}

#2)student Data
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)

#Accessing Values

print(student["name"])
print(student["age"])

#Adding New Data

student["college"] = "IIT"
print(student)

#Updating Values

student["age"] = 21
print(student)

#Removing Data
#using pop()
student.pop("course")
print(student)

#using del

del student["age"]
print(student)

#Looping Through Dictionary
for key, value in student.items():
    print(key, ":", value)

#Useful Dictionary Methods
student.keys()
student.values()
student.items()
student.get("name")
student.clear()
