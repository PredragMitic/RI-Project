from ga import GeneticAlgorithm
from bf import BruteForce
from util import Image, generateImages

images1 = [Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20),
           Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20),
           Image(100, 40), Image(40, 100), Image(20, 30), Image(40, 40), Image(30, 40), Image(20, 20)]
atlas_width = 200
atlas_height = 300

# bf = BruteForce(images, atlas_width, atlas_height)
# bf.run()

images2 = generateImages(10, 200, 30, 1000000)

# Parameters
pop_size = 75  # 80
num_generations = 150  # 100
mutation_prob = 0.1
tour_size = 40
elitism_size = 20

# Run genetic algorithm
ga = GeneticAlgorithm(images1, atlas_width, atlas_height, pop_size,
                      num_generations, tour_size, elitism_size, mutation_prob)
ga.run()
