m = "s" # s or m
income = 10000

if m == "s":
    if income > 32000:
        print(income - income * 0.25)
    else:
        print(income - income * 0.1)
else:
    if income > 64000:
        print(income - income * 0.25)
    else:
        print(income - income * 0.1)    