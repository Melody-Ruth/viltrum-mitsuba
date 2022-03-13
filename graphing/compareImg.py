import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d
r1, g1, b1 = np.loadtxt('default_pixels1.txt', delimiter=',', unpack=True)#Groundtruth
r2, g2, b2 = np.loadtxt('default_pixels2.txt', delimiter=',', unpack=True)#non-antithetic
r3, g3, b3 = np.loadtxt('pixelValues.txt', delimiter=',', unpack=True)#antithetic

def percentDiff(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return (a-b) / ((a+b)/2)

rmseRedNon = 0
justGreen = 0
justGreenAntithetic = 0
for i in range(len(r1)):
    rmseRedNon += (r2[i]-r1[i])**2

for i in range(len(r1)):
    rmseRedNon += (g2[i]-g1[i])**2
    justGreen += (g2[i]-g1[i])**2
    justGreenAntithetic += (g3[i]-g1[i])**2
    #if percentDiff((g2[i]-g1[i])**2, (g3[i]-g1[i])**2) > 1.95:
        #print(i, g1[i], g2[i], g3[i])

for i in range(len(r1)):
    rmseRedNon += (b2[i]-b1[i])**2

rmseRedNon /= 3 * len(r1)
justGreen /= len(g1)
justGreen **= 0.5
justGreenAntithetic /= len(g1)
justGreenAntithetic **= 0.5

#print(rmseRedNon)
print(justGreen)
print(justGreenAntithetic)

rmseRedNon = 0
for i in range(len(r1)):
    rmseRedNon += (r3[i]-r1[i])**2

for i in range(len(r1)):
    rmseRedNon += (g3[i]-g1[i])**2

for i in range(len(r1)):
    rmseRedNon += (b3[i]-b1[i])**2

rmseRedNon /= 3 * len(r1)
#justGreen /= len(g1)
#justGreen **= 0.5

#print(rmseRedNon)
#print(justGreen)