data = [line.strip('\n') for line in open('rosalind_hamm.txt', 'r')]

s = data[0]
t = data[1]
diff_count = 0

for i in range(0, len(s) - 1):
    if s[i] != t[i]:
        diff_count += 1

print diff_count
