#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:09:39 2019

@author: Abdulkadir Kahraman
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file='testfile.csv'
Smoothness=100
dataset=pd.read_csv(file, header=None)
dataset=dataset.iloc[0:,0:].values


def bezier(p):    
    x1=p[0]
    y1=p[1]
    x2=p[2]
    y2=p[3]
    x3=p[4]
    y3=p[5]
    x4=p[6]
    y4=p[7]    
    bx=3*(x2-x1)
    cx=3*(x3-x2)-bx
    dx=x4-x1-bx-cx
    by=3*(y2-y1)
    cy=3*(y3-y2)-by
    dy=y4-y1-by-cy    
    t=np.linspace(0,1,Smoothness)
    Xt=x1 + bx*t + cx*t**2 + dx*t**3
    Yt=y1 + by*t + cy*t**2 + dy*t**3
    return Xt,Yt

for p in dataset:
    X,Y=bezier(p)
    plt.plot(X,Y,False,False,color='black')
    
plt.axis('off')
plt.savefig(file+'.svg')
plt.show()

