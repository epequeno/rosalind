data = [line.strip("\n") for line in open("rosalind_ini3.txt", "r")]

text = data[0]
indices = data[1].split(" ")
firstWordStart = int(indices[0])
firstWordEnd = int(indices[1])
secondWordStart = int(indices[2])
secondWordEnd = int(indices[3])

print text[firstWordStart:firstWordEnd + 1], text[secondWordStart:secondWordEnd + 1]