#example 1
i = 1
while i<=5:
    print(i)
    i += 1 # its very important  without it infinite loop

#example 2 countdown
count = 5

while count > 0:
    print(count)
    count -= 1

 #example 3 break stop the loop
for i in range(1, 10):
    if i == 5:
        break
    print(i)


#skip the current step
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
