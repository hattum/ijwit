# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import csv
from assets.helpers_miro import offsets


class Visualisation():
    """
    Visualisation takes the coordinates of the folded protein
    and plots it in a graph using MatPlotLib. I also makes the required
    csv file output.
    """
    def  __init__(self, title, score, coordinates):
        self.title = title
        self.score = score
        self.coordinates = coordinates
        self.plot_list = [coordinate[1] for coordinate in coordinates]
        self.csv_list = []

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

        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
 
        # plot control points and connecting lines
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-', color='grey')

        # other settings for the graph
        ax.grid()
        ax.axis('equal')
        plt.title(f'Protein: {self.title}\n Score: {self.score}')
        plt.savefig("Visualisation.png")

        print(f"coordinates: {self.coordinates}")

    def directions(self):
        """
        Calculates the corresponding offsets to a fold.
        These will be used in the csv file.
        """
        
        coords = self.coordinates

        # loop over the coordinate list in order to calculte the corresponding offsets to a fold
        for i in range(len(coords) - 1):
            for direction in offsets:
                if coords[i+1][1] == (coords[i][1][0] + offsets[direction][0], coords[i][1][1] + offsets[direction][1]):

                    # append these calculated offsets to self.csv_list
                    self.csv_list.append((coords[i][0], direction))
        self.csv_list.append((coords[-1][0], "0"))
        print(f"coordinates1: {self.coordinates}")
        print(f"Directions are: {self.csv_list}")

    def csv(self):
        """
        Makes the required csv file for visualisation purposes.
        """
        # open a csv file
        with open('Visualisation.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            # write the header
            writer.writerow(["Amino", "Fold"])

            # write the amino acids with their corresponding offset
            for i in range(len(self.csv_list)):
                writer.writerow([self.csv_list[i][0], self.csv_list[i][1]])

            # write the footer
            writer.writerow(["Score:", self.score])