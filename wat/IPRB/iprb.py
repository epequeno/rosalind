import re

data = [line.strip("\n") for line in open("rosalind_subs.txt", "r")]
s = data[0]
t = data[1]

index_list = [m.start() + 1 for m in re.finditer('(?='+t+')', s)]

answer = ""
for i in index_list:
    answer += str(i) + " "

print answer
