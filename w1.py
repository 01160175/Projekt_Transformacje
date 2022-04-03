# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:27:18 2022

@author: zmigr
"""

import numpy as np

from projekt1 import *

t = np.genfromtxt("wsp_inp.txt", delimiter = ',', skip_header = 4)
rows,cols = np.shape(t)

blh = np.zeros((rows,cols))
xy2000 = np.zeros((rows,2))
xy92 = np.zeros((rows,2))

neu = np.zeros((rows,cols))
az_elev_dis = np.zeros(())