path = "text.txt"
mode = "r"
class1 = open (path, mode)
char = class1.read(1)

while char != "":
    print(char)
    char = class1.read(1)



class1.close()