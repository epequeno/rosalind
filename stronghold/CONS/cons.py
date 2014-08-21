# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 17:06:04 2014

@author: Estevan Adrian Pequeno
"""

data = open('rosalind_cons.txt', 'r').read().split()
formatting = ''.join(data).split(">Rosalind_")
sequences = [item[4:] for item in formatting if len(item) > 0]

seq_length = len(sequences[0])


def counter(sequences, letter, n):
    answer = ""
    for i in range(n):
        count = 0
        for seq in sequences:
            if seq[i] == letter:
                count += 1
        answer += str(count) + " "
    return answer

a_data = "A: " + counter(sequences, "A", seq_length)
c_data = "C: " + counter(sequences, "C", seq_length)
g_data = "G: " + counter(sequences, "G", seq_length)
t_data = "T: " + counter(sequences, "T", seq_length)
stats = [a_data, c_data, g_data, t_data]


def consensus_finder(stats, n):
    cons = {}
    for i in stats:
        splits = i.split()
        cons[splits[0]] = splits[n]
    maximum = 0
    top = ''
    for i in cons:
        if cons[i] >= maximum:
            maximum = cons[i]
            top = i
    return top[0]


def finder():
    answer = ''
    for i in range(1, seq_length+1):
        answer += consensus_finder(stats, i)
    return answer

print finder()
print a_data
print c_data
print g_data
print t_data
