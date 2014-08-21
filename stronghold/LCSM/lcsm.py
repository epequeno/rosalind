# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:48:21 2014

@author: steven
"""

data = open('rosalind_lcsm.txt', 'r').read().split()
formatting = ''.join(data).split(">Rosalind_")
sequences = [item[4:] for item in formatting if len(item) > 0]
seq_length = len(sequences[0])

def