import copy

from ibl import IBL
from util import Image, arrange_images, drawImages, imagesArea


class BruteForce:
    def __init__(self, images, width, height):
        self.images = images
        self.n = len(images)
        self.width = width
        self.height = height
        self.imgArea = imagesArea(images)

    def find_next_permutation(self, sequence):
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


    def generate_all_permutations(self, sequence):
        permutations_list = [sequence[:]]

        while self.find_next_permutation(sequence):
            permutations_list.append(sequence[:])

        return permutations_list


    def generate_all_orijentations(self, length):
        orijentations_list = []

        for num in range(2**length):
            bin_str = bin(num)[2:][::-1]
            orijentations = [False] * length
            for i, j in zip(range(len(bin_str)), bin_str):
                if j == '1':
                    orijentations[i] = True
            orijentations_list.append(orijentations)

        return orijentations_list

    def run(self):
        permutations = self.generate_all_permutations(list(range(self.n)))
        orijentations = self.generate_all_orijentations(self.n)



        w_best = float('inf')
        h_best = float('inf')
        best_placed = []

        ibl = IBL(self.width, self.height)
        for perm in permutations:
            for orijent in orijentations:
                placed_images = ibl.place_images(arrange_images(self.images, perm, orijent))
                w, h = ibl.get_bounds()
                if placed_images and w * h < w_best * h_best:
                    w_best = w
                    h_best = h
                    best_placed = copy.deepcopy(placed_images)

        print(self.imgArea / (w_best * h_best))   
        drawImages(best_placed, self.width, self.height, w_best, h_best)
