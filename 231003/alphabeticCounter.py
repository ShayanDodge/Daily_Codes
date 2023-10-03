path = "text.txt"
mode = "r"
infile = open(path, mode)
outfile = open("outText.txt","a")
alpha = "abc"
txt = infile.read()
counter = 0

for ch in alpha:
    for char in txt:
        if ch == char:
            counter += 1
    # print(ch,counter, file = outfile)
    outfile.write(f"{ch} {counter} \n")
    counter = 0

infile.close()
outfile.close()

