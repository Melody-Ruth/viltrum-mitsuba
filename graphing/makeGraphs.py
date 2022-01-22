import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits import mplot3d

x, y, z1, z2, z3 = np.loadtxt('graph5.txt', delimiter=',', unpack=True)
#print(max(z))
#z1 /= max(abs(z1))
#z2 /= max(abs(z2))
#z3 /= max(abs(z3))

#print(z)
#for singleColor in z:
#    if singleColor != 0 and singleColor != 1:
#        print(singleColor)

#plt.scatter(x, y, c=z, label='Integrand with dimensions i, j, k, and l. i is on the x axis and k is on the y axis. j and l are fixed at 0.355903 and 0.0576333, respectively.')

#plt.scatter(x, y, c=z, label='Polynomial approximation for region 54. Dimensions are i, j, k, and l. i is on the x axis and k is on the y axis. j and l are fixed at 0.0749144 and 0.346793, respectively.')
#plt.legend()
#plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z1, label='Actual integrand for region 54. Dimensions are i, j, k, and l. j is on the x axis and l is on the y axis. I and k are fixed at 0.0749144 and 0.346793, respectively.')
ax.scatter3D(x, y, z2, label='Polynomial approximation for region 54. Dimensions are i, j, k, and l. j is on the x axis and l is on the y axis. I and k are fixed at 0.0749144 and 0.346793, respectively.')
plt.legend()
plt.show()

fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.scatter3D(x, y, z2, label='Polynomial approximation for region 54. Dimensions are i, j, k, and l. j is on the x axis and l is on the y axis. I and k are fixed at 0.0749144 and 0.346793, respectively.')
plt.legend()
plt.show()

fig3 = plt.figure()
ax3 = plt.axes(projection='3d')
ax3.scatter3D(x, y, z3, label='Residual for region 54. Dimensions are i, j, k, and l. j is on the x axis and l is on the y axis. I and k are fixed at 0.0749144 and 0.346793, respectively.')
plt.legend()
plt.show()


