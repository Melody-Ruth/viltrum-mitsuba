import matplotlib.pyplot as plt
import numpy as np

X, Y, Z = np.loadtxt('graph7.txt', delimiter=',', unpack=True)

plt.suptitle("Regions with non-zero integrand, zero approximation, and 2 samples per regions")
plt.xlabel('Percent difference for the average error approximating the residual with antithetic or non-antithetic')
plt.ylabel("'Factor': expresses the size of the region (to multiply with later)")

plt.scatter(X, Y, label="non-antithetic")
plt.scatter(X,Z, label="antitheitc")

plt.legend()
plt.show()