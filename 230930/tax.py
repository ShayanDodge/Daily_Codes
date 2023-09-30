maritalStatus = input("Please enter your marital status (s or m) = ")
income =  float(input("please enter your income per year = "))

if maritalStatus == "s":
    if income < 32_000:
        print(f"The tax is %10. So you should pay {income*0.10}")
    else:
        print(f"The tax is %10 for the first 32000 and for the remaining amount is %25. So you should pay {32_000*0.10 + (income-32_000)*0.25}")
else:
    if income < 64_000:
        print(f"The tax is %10. So you should pay {income*0.10}")
    else:
        print(f"The tax is %10 for the first 64000 and for the remaining amount is %25. So you should pay {64_000*0.10 + (income-64_000)*0.25}")
