# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 22:54:58 2014

@author: steven
"""

data = [line.strip("\n") for line in open("rosalind_1b.txt", "r")]

dna = data[0]

codex = {"A": "T", "T": "A", "G": "C", "C": "G"}


def revc(dna):
    comp = ""
    for i in range(0, len(dna)):
        if dna[i] in codex:
            comp += codex[dna[i]]
    return comp[::-1]

print revc(dna)
