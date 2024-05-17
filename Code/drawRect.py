import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def drawRectangles(rectangles, maxX, maxY):
  fig, ax = plt.subplots()

  # Iniciajlni pravougaonik
  ax.add_patch(Rectangle((0, 0), maxX, maxY, fill=False))

  for rect in rectangles:
    x = rect[0]
    y = rect[1]
    w = rect[2]
    h = rect[3]
    o = '--' if rect[4] else '||'

    ax.add_patch(Rectangle((x, y), w, h, fill=False, hatch=o))
    #plt.annotate(i , (x + 40,y + 40))

  ax.plot()
  plt.show()

drawRectangles(
    [[0, 0, 200, 300, 0],
    [200, 0, 300, 300, 1], 
    [500, 200, 300, 500, 1]], 
    1300, 1000)