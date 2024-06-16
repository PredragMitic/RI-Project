import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#random.seed(10)

def drawExample(maxX, maxY):
    fig, ax = plt.subplots()

    # Pravuganik koji predstavlja atlas u koji treba ubaciti slike
    ax.add_patch(Rectangle((0, 0), maxX, maxY, fill=False))
    plt.annotate('A', (10, 10))

    ax.add_patch(Rectangle((50, 50), 200, 150, fill=False, hatch='||', edgecolor='skyblue'))
    ax.add_patch(Rectangle((50, 50), 200, 150, fill=False))
    plt.annotate('P1', (60, 35))
    plt.annotate('h1', (35, 125))
    plt.annotate('w1', (140, 40))

    ax.add_patch(Rectangle((300, 100), 70, 150, fill=False, hatch='--', edgecolor='skyblue'))
    ax.add_patch(Rectangle((300, 100), 70, 150, fill=False))
    plt.annotate('P2', (310, 85))
    plt.annotate('h2', (330, 90))
    plt.annotate('w1', (280, 170))

    ax.plot()
    plt.show()


drawExample(400, 300)

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = None
        self.y = None
        self.rotated = False

    def rotate(self):
        w = self.width
        self.width = self.height
        self.height = w
        self.rotated = not self.rotated


def drawImages(images, maxX, maxY, bound_x, bound_y):
    fig, ax = plt.subplots()

    # Atlas
    ax.add_patch(Rectangle((0, 0), maxX, maxY, fill=False))

    for rect in images:
        x = rect.x
        y = rect.y
        w = rect.width
        h = rect.height
        o = '--' if rect.rotated else '||'

        ax.add_patch(Rectangle((x, y), w, h, fill=False,
                     hatch=o, edgecolor='skyblue'))
        ax.add_patch(Rectangle((x, y), w, h, fill=False))

    ax.add_patch(Rectangle((0, 0), bound_x, bound_y,
                 fill=False, edgecolor='r'))

    ax.plot()
    plt.show()

def arrange_images(images, perm, orijent):
    arranged = []
    for i in range(len(images)):
        image = images[perm[i]]
        if orijent[i] is not image.rotated:
          image.rotate()
        arranged.append(image)

    return arranged

def generateImages(minDim, maxDim, n, maxArea):
    # Ukupna povrsina slika
    area = 0
    images = []

    for _ in range(n):
        w = random.randint(minDim, maxDim)
        h = random.randint(minDim, maxDim)
        image = Image(w, h)
        area = area + w * h
        if area >= maxArea:
            break
        images.append(image)

    return images

def imagesArea(images):
    sum = 0
    for img in images:
        sum = sum + img.width * img.height

    return sum