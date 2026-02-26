def count_vowels(s):
    count=0

    for char in s:
        if char in "aeiou":
            print(char)
            count+=1
    return count
print("total vowels are: ",count_vowels("education"))