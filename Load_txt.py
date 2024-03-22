# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:08:55 2024

@author: dsign
"""

import numpy as np
import matplotlib.pyplot as plt
hh = '19'
mm = '00'
date ='20230728'

fsample=2000
# 202307280000_2000Hz_dc.gz.txt.gz

file =date+hh+mm+'_'+str(fsample)+'Hz_'+'dc.gz.txt.gz'
data=np.loadtxt('G:\\Il mio Drive\\2023\\20NRM DC grid\WP2\\'+file,delimiter=',')

N=len(data[:,0])
t=np.linspace(0,N/fsample,N)

V=np.reshape(data[:,0],(2000,int(N/2000)))
AV=np.mean(V,axis=0)
I=np.reshape(data[:,1],(2000,int(N/2000)))
AI=np.mean(I,axis=0)
# plt.figure()
# plt.plot(t,data)
# plt.grid()

plt.figure()
plt.plot(AV)

plt.figure()
plt.plot(AI)