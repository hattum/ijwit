# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

class Visualisation():
    """
    Visualisation takes the coordinates of the folded protein
    and plots it in a graph using MatPlotLib.
    """
    def  __init__(self, title, score, coordinates):
        self.title = title
        self.score = score
        self.coordinates = coordinates
        self.plot_list = [coordinate[1] for coordinate in coordinates]

    def plot(self):
        """
        Method to plot the graph. 
        """
        fig, ax = plt.subplots()
        Path = mpath.Path   
        path_data = []

        # make a list of the path to be plotted by looping over the coordinates list
        for i in range(len(self.coordinates)):
            if i == 0:
                path_data.append((Path.MOVETO, (self.plot_list[i])))
            else:
                path_data.append((Path.LINETO, (self.plot_list[i])))

        # check print statement
        print(f'path list: {path_data}')
        
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
 
        # plot control points and connecting lines
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-', color='grey')

        # other settings for the graph
        # plt.legend()
        ax.grid()
        ax.axis('equal')
        plt.title(f'Protein: {self.title}\n Score: {self.score}')
        plt.savefig("Visualisation.png")