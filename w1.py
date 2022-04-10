# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:27:18 2022

@author: zmigr
"""

import numpy as np
from projekt1 import *

geo = Transformacje(model = "wgs84")

t = np.genfromtxt("wsp_inp.txt", delimiter = ',', skip_header = 4)
rows,cols = np.shape(t)

blh = np.zeros((rows,cols))
xy2000 = np.zeros((rows,2))
xy92 = np.zeros((rows,2))

neu = np.zeros((rows,cols))
az_elev_dis = np.zeros(())



X = t[:,0]
Y = t[:,1]
Z = t[:,2]


print(geo.xyz_2_blh(X, Y, Z))

np.savetxt("wsp_out.txt", t, delimiter=',', fmt = ['%10.2f', '%10.2f', '%10.3f'], header = 'Konwersja współrzędnych geodezyjnych \\ Jakub Żmigrodzki')