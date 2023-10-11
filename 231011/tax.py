salary = int(input ("please enter your salary = "))
maritalStatus = input("pleaes enter s for single and m for marrid = ")


if maritalStatus == "s":
    if salary < 32000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25
else:
    if salary < 64000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25


print (tax)