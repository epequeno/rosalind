data = [line.strip("\n") for line in open("rosalind_ini6.txt", "r")]
words = data[0].split(" ")

def countWords(wordList):
	answers = {}
	for i in words:
		if i in words:
			answers[i] = 1 + answers.get(i, 0)
	for i in answers:
		print i, answers[i]
countWords(words)