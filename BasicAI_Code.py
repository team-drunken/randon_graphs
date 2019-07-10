# import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
print('This is working')
fig = plt.figure()
ax = Axes3D(fig)
# ax = fig.add_subplot(111, projection='3d')
X = [6, 2, 4, 7, 2]
Y = [1, 6, 3, 7, 0]
Z = [8, 5, 3, 4, 9]
ax.plot(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D')
plt.show()
