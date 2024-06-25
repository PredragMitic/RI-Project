from ga import GeneticAlgorithm
from bf import BruteForce
from util import Image, generateImages
import time

start = time.time()

images1 = [Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20)]
images2 = [Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20), Image(60, 50), Image(50, 70)]


atlas_width = 300
atlas_height = 240

#bf = BruteForce(images1, atlas_width, atlas_height)
#bf.run()

#images2 = generateImages(10, 200, 30, 1000000)

images3 = [Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20), Image(40, 50),
            Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20), Image(50, 30),
            Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20)]

# Parametri
pop_size = 100
num_generations = 150
mutation_prob = 0.05
tour_size = 25
elitism_size = 15

ga = GeneticAlgorithm(images3, atlas_width, atlas_height, pop_size, num_generations, tour_size, elitism_size, mutation_prob)
ga.run()


end = time.time()
print(end - start)