import math

data = [line.strip("\n") for line in open("rosalind_ini2.txt", "r")]
values = data[0].split(" ")
x = int(values[0])
y = int(values[1])

def findHypot(x, y):
	return x**2 + y**2

print findHypot(x, y)