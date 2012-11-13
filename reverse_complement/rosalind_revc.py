data = [line for line in open('rosalind_revc.txt','r')]

seq = data[0]

def make_rev_complement(seq):
    complement = []
    for base in seq:
        if base == 'A':
            complement.append('T')
        if base == 'T':
            complement.append('A')
        if base == 'G':
            complement.append('C')
        if base == 'C':
            complement.append('G')
    return ''.join(complement)[::-1]

print make_rev_complement(seq)