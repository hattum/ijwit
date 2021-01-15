import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

class Visualisation():

    # initialize the Visualization class
    def  __init__(self, title, score, coordinates):
        self.title = title
        self.score = score
        self.coordinates = coordinates

    # plot the graph
    def plot(self):
        fig, ax = plt.subplots()
        Path = mpath.Path   
        path_data = []

        for i in range(len(self.coordinates)):
            if i == 0:
                path_data.append((Path.MOVETO, (self.coordinates[i])))
            else:
                path_data.append((Path.LINETO, (self.coordinates[i])))

        print(f'path list: {path_data}')
        
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
 
        # plot control points and connecting lines
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-', color='grey')

        ax.grid()
        ax.axis('equal')
        plt.title(f'Protein: {self.title}\n Score: {self.score}')
        plt.legend()
        plt.savefig("Visualisation.png")