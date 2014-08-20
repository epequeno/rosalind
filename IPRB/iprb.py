# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:30:35 2014

@author: steven
"""

import random

dataset = [int(i) for i in open('rosalind_iprb.txt', 'r').read().split()]

# Punnet
dom_dom = 1.0
dom_het = 1.0
dom_rec = 1.0
het_rec = 0.5
het_het = 0.75
rec_rec = 0.0

population = []

population.extend(['dom'] * dataset[0])
population.extend(['het'] * dataset[1])
population.extend(['rec'] * dataset[2])


def chance_of_dominant():
    male = random.choice(population)
    female = random.choice(population)
    if male == 'dom' or female == 'dom':
        return dom_dom
    elif male == 'het' and female == 'rec':
        return het_rec
    elif male == 'rec' and female == 'het':
        return het_rec
    elif male == 'het' and female == 'het':
        return het_het
    else:
        return rec_rec


def group_chances(n):
    results = 0
    for i in range(n):
        results *= chance_of_dominant()
    return results

print group_chances(100)
