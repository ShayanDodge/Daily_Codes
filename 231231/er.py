num1 = input ("please enter an number ")
list1 = []
list2 = []
list = []
while num1 != "":
    num1 = int(num1)
    list.append(num1)
    num1 = input ("please enter an number ")

print(list[int(len(list) / 2)])