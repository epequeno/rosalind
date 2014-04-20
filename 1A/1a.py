# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 22:02:48 2014

@author: steven
"""

data = [line.strip("\n") for line in open("rosalind_1a.txt", "r")]

seq = data[0]
k = int(data[1])

def kmer(text, k):
    kmers = {}
    for i in range(0, len(text) - 1):
        test = text[i:i+k]
        if len(test) < k:
            pass
        else:
            kmers[test] = 1 + kmers.get(test, 0)
    top = 0
    for val in kmers.values():
        if val >= top:
            top = val
    answer = [k for k,v in kmers.items() if v == top]
    return answer
    
solution = ""
for i in kmer(seq, k):
    solution += i + " "
print solution