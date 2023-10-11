from csv import reader
with open ("Book1.csv","r") as infile:
    csvReader = reader(infile)
    for line in csvReader:
        print(line[0])