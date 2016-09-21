# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 02:44:56 2016

@author: tep
"""
import numpy as np

def distance(i, j, layer_1):
    
    size = layer_1 ** 0.5 
    i = [i // size, i % size]
    j = [j // size, j % size]
    
    if abs( (i[0] % size) - (j[0] % size) ) % (size-1) < 2  and abs( (i[1] % size) - (j[1] % size ) ) % (size-1)  < 2:
        return 1
    else:
        return 0
    

def layer_two_weights(layer_1, layer_2):
    g = np.zeros((layer_1, layer_2))
    
    for i in range(layer_2):
        
        for j in range(layer_1):
            
            g[i, j] = distance(i, j, layer_1)
    return g
    
a = distance(0,223,25)
print (a)

g = layer_two_weights(25,25)
print(g)