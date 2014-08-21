data = [seq for seq in open('rosalind_rna.txt', 'r')]

dna = data[0]

rna = dna.replace("T", "U")
print rna