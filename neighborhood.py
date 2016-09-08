# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:17:59 2016

@author: tep
"""

import numpy as np

def neighborhood(matrix, x, y, size=3):
    
    (row, column) = np.shape(matrix)
    local = (size - 1) // 2
    pooled = 0
    
    assert size <= row + 1
    assert size <= column + 1
    assert size % 2 == 1
    
    if ( (x - local) < 0 ):
        h_shift = local - x
        matrix = np.roll(matrix, h_shift, axis = 1)
        x = x + h_shift
    
    elif ( (x + local) > row):
        h_shift = local + x
        matrix = np.roll(matrix, -h_shift, axis = 1)
        x = x - h_shift
    
    if  ( (y - local) < 0 ):
        v_shift = local - y
        matrix = np.roll(matrix, v_shift, axis = 0)
        y = y + v_shift
    
    elif ( (y - local) > column ):
        v_shift = local - y
        matrix = np.roll(matrix, -v_shift, axis = 0)
        y = y - v_shift
    
    for i in range(x - local, x + local + 1):
        
        for j in range(y - local, y + local + 1):
            
            pooled = pooled + matrix[i,j]
            
    return pooled    

    
        
        
        
        
        
        