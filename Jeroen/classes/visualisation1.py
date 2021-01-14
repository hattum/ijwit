
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

protein = "PHPPHPHH"
coordinates = [("P", (0, 0)), ("H", (0, 1)), ("p", (-1, 1)), ("p", (-1, 2)), ("H", (0, 2)), ("p", (1, 2)), ("H", (1, 1)), ("H", (1, 0)), ("H", (1, -5))]

'''
for i in range(len(self.coordinates)):
            if i == 0:
                path_data.append((Path.MOVETO, (self.coordinates[i])))
            else:
                path_data.append((Path.LINETO, (self.coordinates[i])))
'''
for i in range(len(coordinates)):
	plt.plot(coordinates[i][1], coordinates[i+1][1])

plt.savefig("Visualisation1.png")

"""
x = [1, 2, 3]
y = [1, 2, 3]

plt.scatter(x,y,color='red',zorder=2)
plt.plot(x,y,color='grey',zorder=1)

plt.title("Connected Scatterplot points with line")
plt.xlabel("x")
plt.ylabel("sinx")

plt.savefig("Visualisation1.png")

"""


"""
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 

# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "green", 
			marker= "*", s=30) 

# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 

# function to show the plot 
plt.savefig("Visualisation1.png")

  
plt.grid()


ax.grid()
ax.axis('equal')
plt.title(f'Protein: d{protein}')
plt.legend()
plt.savefig("Visualisation1.png")
"""

