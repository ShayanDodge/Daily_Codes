max = int(input("please enter the maximum number = "))
i = 1

while i < max:
    if i % 5 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1