import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d
r1, g1, b1 = np.loadtxt('dragon_ground_truth_15500.txt', delimiter=',', unpack=True)#Groundtruth
r2, g2, b2 = np.loadtxt('non_antithetic_pixels.txt', delimiter=',', unpack=True)#non-antithetic
r3, g3, b3 = np.loadtxt('antithetic_pixels.txt', delimiter=',', unpack=True)#antithetic

def percentDiff(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return (a-b) / ((a+b)/2)

rmseGen = 0
rmseGenAnti = 0
justGreen = 0
justGreenAntithetic = 0
justRed = 0
justRedAntithetic = 0
justBlue = 0
justBlueAntithetic = 0
for i in range(len(r1)):
    justRed += (r2[i]-r1[i])**2
    justRedAntithetic += (r3[i]-r1[i])**2
    rmseGen += (r2[i]-r1[i])**2
    rmseGenAnti += (r3[i]-r1[i])**2
    #if (percentDiff((r2[i]-r1[i])**2, (r3[i]-r1[i])**2) > 1.5):
        #print("red", i, r1[i], r2[i], r3[i])

for i in range(len(r1)):
    rmseGen += (g2[i]-g1[i])**2
    rmseGenAnti += (g3[i]-g1[i])**2
    justGreen += (g2[i]-g1[i])**2
    justGreenAntithetic += (g3[i]-g1[i])**2
    #if (percentDiff((g2[i]-g1[i])**2, (g3[i]-g1[i])**2) > 1.5):
        #print("green", i, g1[i], g2[i], g3[i])

for i in range(len(r1)):
    #rmseRedNon = rmseRedNon
    justBlue += (b2[i]-b1[i])**2
    justBlueAntithetic += (b3[i]-b1[i])**2
    rmseGen += (b2[i]-b1[i])**2
    rmseGenAnti += (b3[i]-b1[i])**2
    #if (percentDiff((b2[i]-b1[i])**2, (b3[i]-b1[i])**2) > 1.5):
        #print("blue", i, b1[i], b2[i], b3[i])

rmseGen /= 3*len(r1)
rmseGen **= 0.5
rmseGenAnti /= 3*len(r1)
rmseGenAnti **= 0.5
justBlue /= len(r1)
justBlue **= 0.5
justBlueAntithetic /= len(r1)
justBlueAntithetic **= 0.5
justGreen /= len(g1)
justGreen **= 0.5
justGreenAntithetic /= len(g1)
justGreenAntithetic **= 0.5
justRed /= len(g1)
justRed **= 0.5
justRedAntithetic /= len(g1)
justRedAntithetic **= 0.5

#print("red")
#print(justRed)
#print(justRedAntithetic)
#print("blue")
#print(justBlue)
#print(justBlueAntithetic)
#print("green")
#print(justGreen)
#print(justGreenAntithetic)
#print("general")
print(rmseGen,rmseGenAnti,sep=',')

