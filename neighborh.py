# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 02:44:56 2016

@author: tep
"""
import numpy as np

def distance(i, j, layer_1):
    """ This function measures the distance between element i and j. The distance 
    here is the distance between element i and j once the row vector has been 
    reshaped into a square matrix"""
    
    size = layer_1 ** 0.5 
    i = [i // size, i % size]
    j = [j // size, j % size]
    
    if abs( (i[0] % size) - (j[0] % size) ) % (size-1) < 2  and abs( (i[1] % size) - (j[1] % size ) ) % (size-1)  < 2:
        return 1
    else:
        return 0
    

def layer_two_weights(layer_2, layer_1):
    """ This function takes in layer 2 and layer 1 size and returns the layer 2
    connection. This is currently only working for the case when (# of layer 2
    units) = (# of layer 1 units) """
    
    g = np.zeros((layer_2, layer_1))
    
    for i in range(layer_2):
        
        for j in range(layer_1):
            
            g[i, j] = distance(i, j, layer_1)
    return g


    

