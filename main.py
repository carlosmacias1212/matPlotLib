from random import randint
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


convexHull = [[15, 4], [8, 20], [-14, 12], [-20, 7], [-17, -16], [-12, -19], [6, -19], [15, -13], [15, 4]]


# Set up x and y axis's for plotting points

fig, ax = plt.subplots()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)

class GUI:




       ax.text(-40, 30, "Brute Force runtime:", weight='bold')
       ax.text(-40, 24, "Quick Hull runtime:", weight='bold')
       ax.text(-40, -15, "Convex Hull Points:", weight='bold')
       for i in range(len(convexHull)):
              print(i)
              ax.text(-30, -23 - (3 * i), "(" + str(convexHull[i][0]) + ", " + str(convexHull[i][1]) + ")")

 
       def plot_points(self):
              #global pts
              #pts.remove()
              pointsList = []
              for i in range(20):
                     x = randint(-20, 20)
                     y = randint(-20, 20)
                     pointsList.append([x, y])


              data = np.array(pointsList)
              x, y = data.T
              pts = plt.scatter(x, y)





       # Update array of points to show convex hull line segments

       def draw_hull(self):

              hull = np.array(convexHull)
              draw_x, draw_y = hull.T

              plt.plot(draw_x, draw_y)
              plt.show()



       # Randomize points
       axrand = plt.axes([0.6, 0.05, 0.14, 0.075])
       brand = Button(axrand, 'Plot Points')
       brand.on_clicked(plot_points)

       # Button will call draw_hull in order to plot line segments in convex hull
       axnext = plt.axes([0.85, 0.05, 0.14, 0.075])
       bnext = Button(axnext, 'Draw Hull')
       bnext.on_clicked(draw_hull)



       plt.sca(fig.axes[0])
       plt.margins(.4, .6)
       plt.show()
