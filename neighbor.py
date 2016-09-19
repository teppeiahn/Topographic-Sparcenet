# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 01:08:59 2016

@author: tep
"""
import numpy as np


def neighbor(layer_1, s = 3):
    
    g = np.zeros((layer_1, layer_1))
    local = 1
    size = int((layer_1)**(.5))
   
    for i in range(layer_1):
        
        for j in range(layer_1):
            h = np.zeros((size, size))
            temp1 = i
            k = 0
            while k < 3:
                temp2 = j
                m = 0
                while m < 3:
                    h[(temp1 - local) % size, (temp2 - local) % size] = 1
                    temp2 = temp2 + 1
                    m = m + 1
                    
                temp1 = temp1 + 1
                k = k + 1
            g[i] = h.flatten()
    
    return g
                
print (neighbor(16,16))               
                   
                    
                    
                    
                    
                    
                    
                    
                    
            
            