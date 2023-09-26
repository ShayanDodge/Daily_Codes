infile = open("students.txt","r")
line = infile.readline()
for char in line:
    print(char)
# list = []
# while line:
#     list.append(float(line))
#     print(line)
#     line = infile.readline()

# print(list)
infile.close()