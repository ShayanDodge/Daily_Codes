income = float(input("please enter your income = "))
s_m = input("please enter your matital status (s or m)= ")

if s_m == "s":
    if (income < 32000):
        print ("tax = ", income * 0.1)
    else:
        print("tax = ", income * 0.25)
else:
    if (income < 64000):
        print("tax = ", income * 0.1)
    else:
        print("tax = ", income * 0.25)