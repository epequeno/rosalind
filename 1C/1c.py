# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 02:28:26 2014

@author: steven
"""

data = [line.strip("\n") for line in open("rosalind_1c.txt", "r")]

substring = data[0]
genome = data[1]

def find(substring, genome):
    indices = ""
    for i in range(0, len(genome)):
        if substring == genome[i: i + len(substring)]:
           indices += str(i) + " "
    return indices
    
print find(substring, genome)