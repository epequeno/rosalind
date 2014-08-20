# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:30:35 2014

@author: steven
"""

import random

dataset = [int(i) for i in open('rosalind_iprb.txt', 'r').read().split()]

total = sum(dataset)
dominant_probibility = dataset[0] / float(total)
hetero_probibility = dataset[1] / float(total)
recessive_probibility = dataset[2] / float(total)

population = [dominant_probibility, hetero_probibility, recessive_probibility]

male = random.choice(population)
female = random.choice(population)

# Punnet probibilities
dom_dom = 1.0
dom_het = 1.0
dom_rec = 1.0
het_rec = 0.5
het_het = 0.75
rec_rec = 0.0


