import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d
r1, g1, b1 = np.loadtxt('default_pixels1.txt', delimiter=',', unpack=True)#Groundtruth
r2, g2, b2 = np.loadtxt('default_pixels2.txt', delimiter=',', unpack=True)#non-antithetic
r3, g3, b3 = np.loadtxt('default_pixels3.txt', delimiter=',', unpack=True)#antithetic

rmseRedNon = 0
for i in range(len(r1)):
    rmseRedNon += (r2[i]-r1[i])**2

for i in range(len(r1)):
    rmseRedNon += (g2[i]-g1[i])**2

for i in range(len(r1)):
    rmseRedNon += (b2[i]-b1[i])**2

rmseRedNon /= 3 * len(r1)

print(rmseRedNon)

rmseRedNon = 0
for i in range(len(r1)):
    rmseRedNon += (r3[i]-r1[i])**2

for i in range(len(r1)):
    rmseRedNon += (g3[i]-g1[i])**2

for i in range(len(r1)):
    rmseRedNon += (b3[i]-b1[i])**2

rmseRedNon /= 3 * len(r1)

print(rmseRedNon)