#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:53:32 2022

@author: akshayghosh

/Users/akshayghosh/wavelet_analysis/adjust_bin_width.py
"""

import numpy as np

def adjust_bin_width(x,t,new_bin_width):
    
    n = len(x)
    initial_bin_width = (np.max(t) - np.min(t))/n
    q = new_bin_width/initial_bin_width # q is bin_multiplier
    
    x2 = np.reshape(x,(int(n/q),int(q)))
    t2 = np.reshape(t,(int(n/q),int(q)))
    
    x2_avg = np.mean(x2,axis = 1)
    t2_avg = np.mean(t2,axis = 1)
    
    x_adjust = np.reshape(x2_avg,len(x2_avg))
    t_adjust = np.reshape(t2_avg,len(t2_avg))
    
    # x_adjust = np.concatenate(x2_avg)
    # t_adjust = np.concatenate(t2_avg)

    return(x_adjust,t_adjust)