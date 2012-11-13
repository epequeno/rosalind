data = [nucleotide for nucleotide in open('rosalind_dna.txt', 'r')]

seq = data[0]

print len(seq), seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")
