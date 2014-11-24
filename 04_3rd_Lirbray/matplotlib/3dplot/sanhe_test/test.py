##encoding=utf8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import time

df = pd.read_csv(r"grid_population.csv", header = 0, index_col = False)
x, y, z = df["center_la"].values, df["center_lg"].values, df["population"].values[np.newaxis]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c="r", marker="o")

plt.show()