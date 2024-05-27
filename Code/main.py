import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import copy


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


class IBL:
    def __init__(self, container_width, container_height):
        self.container_width = container_width
        self.container_height = container_height
        self.placed_images = []

    def can_place(self, image, x, y):
        # Provera da li se slika uklapa u kontejner
        if x + image.width > self.container_width or y + image.height > self.container_height:
            return False
        # Provera da li se preklapa sa vec postavljenim slikama
        for placed_image in self.placed_images:
            if (x < placed_image.x + placed_image.width and x + image.width > placed_image.x and
                    y < placed_image.y + placed_image.height and y + image.height > placed_image.y):
                return False
        return True

    def find_position(self, image):
        best_x, best_y = None, None
        min_y = float('inf')

        # Razmotri sve moguce pozicije slike
        for placed_image in self.placed_images:
            positions = [(placed_image.x, placed_image.y + placed_image.height),
                         (placed_image.x + placed_image.width, placed_image.y)]
            for (x, y) in positions:
                if self.can_place(image, x, y):
                    # Provera koliko je mozemo pribiti levo
                    # original_x = x
                    while x > 0 and self.can_place(image, x - 1, y):
                        x -= 1
                    if y < min_y or (y == min_y and x < best_x):
                        min_y = y
                        best_x, best_y = x, y

        # Prover donjeg levog ulgla
        if self.can_place(image, 0, 0):
            best_x, best_y = 0, 0

        return best_x, best_y

    def update_bounds(self, image):
        x_border = image.x + image.width
        y_border = image.y + image.height

        if x_border > self.bound_width:
            self.bound_width = x_border

        if y_border > self.bound_height:
            self.bound_height = y_border

    def get_bounds(self):
        return self.bound_width, self.bound_height

    def place_images(self, images):
        self.placed_images.clear()
        self.bound_width = 0
        self.bound_height = 0
        for image in images:
            x, y = self.find_position(image)
            if x is not None and y is not None:
                image.x, image.y = x, y
                self.placed_images.append(image)
                self.update_bounds(image)

        if len(self.placed_images) < len(images):
            self.bound_height = float('inf')
            self.bound_width = float('inf')
            return []
        
        return self.placed_images


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


def generate_all_orijentations(length):
    orijentations_list = []

    for num in range(2**length):
        bin_str = bin(num)[2:][::-1]
        orijentations = [False] * length
        for i, j in zip(range(len(bin_str)), bin_str):
            if j == '1':
                orijentations[i] = True
        orijentations_list.append(orijentations)

    return orijentations_list

def arrange_images(images, perm, orijent):
    arranged = []
    for i in range(len(images)):
        image = images[perm[i]]
        if orijent[i]:
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

def drawImages(images, maxX, maxY, bound_x, bound_y):
  fig, ax = plt.subplots()

  # Atlas
  ax.add_patch(Rectangle((0, 0), maxX, maxY, fill=False))

  for image in images:
    x = image.x
    y = image.y
    w = image.width
    h = image.height
    o = '--' if image.rotated else '||'

    ax.add_patch(Rectangle((x, y), w, h, fill=False, hatch=o, edgecolor='skyblue'))
    ax.add_patch(Rectangle((x, y), w, h, fill=False))


  ax.add_patch(Rectangle((0, 0), bound_x, bound_y, fill=False, edgecolor='r'))

  ax.plot()
  plt.show()


def experiment(n):
    permutations = generate_all_permutations(list(range(n)))
    orijentations = generate_all_orijentations(n)

    images = generateImages(20, 200, n, 120000)
    if len(images) < n:
      print('Nedovoljno slika')

    atlas_width = 400
    atlas_height = 300

    w_best = float('inf')
    h_best = float('inf')
    best_placed = []

    for perm in permutations:
        for orijent in orijentations:
            ibl = IBL(atlas_width, atlas_height)
            placed_images = ibl.place_images(arrange_images(images, perm, orijent))
            w, h = ibl.get_bounds()
            if w * h < w_best * h_best:
                w_best = w
                h_best = h
                best_placed = copy.deepcopy(placed_images)
            
    drawImages(best_placed, atlas_width, atlas_height, w_best, h_best)

    

experiment(6)