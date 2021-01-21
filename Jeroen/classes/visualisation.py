
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

protein = "PHPPHPHH"
tuple_list = [("P", (0, 0)), ("H", (0, 1)), ("p", (-1, 1)), ("p", (-1, 2)), ("H", (0, 2)), ("p", (1, 2)), ("H", (1, 1)), ("H", (1, 0)), ("H", (1, -5))]
coordinates = [coordinate[1] for coordinate in tuple_list]
print(coordinates)

fig, ax = plt.subplots()
Path = mpath.Path
path_data = []



for i in range(len(coordinates)):
    if i == 0:
        path_data.append((Path.MOVETO, (coordinates[i])))
    else:
        path_data.append((Path.LINETO, (coordinates[i])))
print(path_data)

"""
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)

# plot control points and connecting lines
x, y = zip(*path.vertices)
points = ax.plot(x, y, 'go', ms=10, color='green')
line, = ax.plot(x, y, 'go-', color='grey')


ax.grid()
ax.axis('equal')
plt.title(f'Protein: d{protein}')
plt.legend()
plt.savefig("Visualisation.png")
"""