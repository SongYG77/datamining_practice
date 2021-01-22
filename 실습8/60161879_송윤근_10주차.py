import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection = '3d')
theta = np.linspace(0,(2 * np.pi),500)
r = np.linspace(-2,2,500)
theta , r = np.meshgrid(theta,r)

X = r * np.cos(theta)
Y = r * np.sin(theta)
Z = 4 * r

ax.plot_wireframe(X,Y,Z)
plt.show()
