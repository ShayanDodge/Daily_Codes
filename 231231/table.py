table = []
row = []

for i in range(10):
    for j in range(10):
        row.append(j)
    table.append(row)

for i in range(10):
    for j in range(10):
        print(table[i][j], end = " ") 
    print()

