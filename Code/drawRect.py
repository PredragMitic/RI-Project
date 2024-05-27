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


def generateRectangles(minDim, maxDim, n, maxArea):
  area = 0
  rectangles = []

  for i in range(n):
    w = random.randint(minDim, maxDim)
    h = random.randint(minDim, maxDim)
    area = area + w * h
    if area >= maxArea:
      break
    rectangles.append([w, h])

  print(area)
  return rectangles

rectangles = generateRectangles(200, 600, 10, 1300000)

def find_next_permutation(sequence):
    k = len(sequence) - 2
    while k >= 0 and sequence[k] >= sequence[k + 1]:
        k -= 1

    if k == -1:
        return False

    l = len(sequence) - 1
    while sequence[l] <= sequence[k]:
        l -= 1

    sequence[k], sequence[l] = sequence[l], sequence[k]
    sequence[k + 1:] = reversed(sequence[k + 1:])
    return True

def generate_all_permutations(sequence):
    permutations_list = [sequence[:]]

    while find_next_permutation(sequence):
        permutations_list.append(sequence[:])

    return permutations_list

perm = generate_all_permutations(rectangles)
print(len(perm))