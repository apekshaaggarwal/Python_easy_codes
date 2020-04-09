# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:43:22 2020

@author: Apeksha
"""

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slopel, interceptl, rvaluel, pvaluel, stderrl = stats.linregress(x,y)

nyfunc1 = lambda x : slopel * x + interceptl

pedictedy = list(map(nyfunc1, x))
plt.scatter(x,y)
plt.plot(x,pedictedy)
plt.show()


#predicted y is
'''
predictedy = [94.3495217071376,
 90.84694628403238,
 89.09565857247976,
 90.84694628403238,
 99.60338484179543,
 73.33406916850626,
 99.60338484179543,
 87.34437086092716,
 96.10080941869022,
 83.84179543782193,
 82.09050772626932,
 87.34437086092716,
 92.59823399558499]'''