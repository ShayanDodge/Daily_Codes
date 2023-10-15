password = "hello"
for char in password:
    if char != password[-1]:
        print(char, end = ",")
    else:
        print(char)