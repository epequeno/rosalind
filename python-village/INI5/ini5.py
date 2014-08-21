data = [line.strip("\n") for line in open("rosalind_ini5.txt", "r")]

def evenLines(text):
	lineNum = 1
	for line in data:
		if lineNum % 2 == 0:
			print line
			lineNum += 1
		else:
			lineNum += 1

evenLines(data)