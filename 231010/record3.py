with open ("data3.txt", "r") as infile:
    line = infile.readline()
    country = []
    population = []
    while line != "":
        for i in range(len(line)):
            if line[i].isdigit():
                break
        country.append(line[:i].strip())
        population.append(line[i:].strip())
        line = infile.readline()

for i in range(len(country)):
    print(country[i], "=", population[i])