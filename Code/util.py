import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def drawExample(maxX, maxY):
    fig, ax = plt.subplots()

    # Pravuganik koji predstavlja atlas u koji treba ubaciti slike
    ax.add_patch(Rectangle((0, 0), maxX, maxY, fill=False))
    plt.annotate('A', (10, 10))

    ax.add_patch(Rectangle((50, 50), 200, 150, fill=False, hatch='||'))
    plt.annotate('P1', (60, 35))
    plt.annotate('h1', (35, 125))
    plt.annotate('w1', (140, 40))

    ax.add_patch(Rectangle((300, 100), 70, 150, fill=False, hatch='--'))
    plt.annotate('P2', (310, 85))
    plt.annotate('h2', (330, 90))
    plt.annotate('w1', (280, 170))

    ax.plot()
    plt.show()


drawExample(400, 300)
