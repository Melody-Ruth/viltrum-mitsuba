import matplotlib.pyplot as plt
import numpy as np

X, Y, Z = np.loadtxt('pumpkin_rmse', delimiter=',', unpack=True)

#plt.suptitle("Regions with non-zero integrand, zero approximation, and 2 samples per regions")
#plt.xlabel('Percent difference for the average error approximating the residual with antithetic or non-antithetic')
#plt.ylabel("'Factor': expresses the size of the region (to multiply with later)")

plt.suptitle("RMSE comparison")
plt.xlabel('samples per pixel')
plt.ylabel("RMSE")

plt.plot(X, Y, '-o', label="non-antithetic")
plt.plot(X, Z, '-o', label="antitheitc")

#plt.plot(X, Y2, '-o', label="non-antithetic (32 scale)")
#plt.plot(X,Z2, '-o', label="antitheitc (32 scale)")

plt.legend()
plt.show()