data = [line.strip("\n") for line in open("rosalind_ini4.txt")]

values = data[0].split(" ")

start = int(values[0])
end = int(values[1])

numbers = [x for x in range(start, end + 1) if x % 2 != 0]

def findSum():
	total = 0
	for i in numbers:
		total += i
	return total

print findSum()