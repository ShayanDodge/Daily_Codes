# Splitting string and removing punctuation marks
inputFile = open("data.txt", "r")
for line in inputFile:
    line = line.rstrip()
    wordList = line.split(",")
    for word in wordList:
        word = word.rstrip(".,?!")
        print(word)
inputFile.close()
