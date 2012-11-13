data = [line.strip('\n') for line in open('rosalind_gc.txt', 'r')]

raw = ''.join(data).split('>')

def find_max_gc(data):
	results = []
	for sample in data:
		if len(sample) < 1:
			pass
		else:
			title = sample[:13]
			seq = sample[13:]
			g_count = seq.count("G")
			c_count = seq.count("C")
			gc_count = g_count + c_count
			total = float(len(seq))
			results.append(((gc_count / total) * 100, title))
	results.sort(reverse=True)
	return results

answers = find_max_gc(raw)
print answers[0][1]
print "%s%%" % answers[0][0]
