import random
from copy import deepcopy
from util import drawImages, arrange_images, imagesArea
from ibl import IBL

class Individual:
    def __init__(self, images, width, height):
        self.images = images
        self.imgArea = imagesArea(images)
        self.n = len(images)
        self.width = width
        self.height = height
        self.code = self.createCode()
        self.fitness = self.calc_fitness()

    def createCode(self):
        order = list(range(self.n))
        random.shuffle(order)
        return order + [random.random() < 0.5 for _ in range(self.n)]
        
    def calc_fitness(self):
        ibl = IBL(self.width, self.height)
        ibl.place_images(arrange_images(self.images, self.code[:self.n], self.code[self.n:]))
        w, h = ibl.get_bounds()
        return self.imgArea / (w*h)

    def update_fitness(self):
        self.fitness = self.calc_fitness()

class GeneticAlgorithm:
    def __init__(self, images, width, height, pop_size, 
        num_generations, tournament_size, elitism_size, p):
        self.images = images
        self.width = width
        self.height = height
        self.pop_size = pop_size
        self.n = len(images)
        self.num_generations = num_generations
        self.tournament_size = tournament_size
        self.elitism_size = elitism_size
        self.mutation_prob = p
        self.population = self.initialize_population()
        self.imgArea = imagesArea(images)

    def show(self, chromosome):
        ibl = IBL(self.width, self.height)
        placed_images = ibl.place_images(arrange_images(self.images, chromosome[:self.n], chromosome[self.n:]))
        w, h = ibl.get_bounds()
        drawImages(placed_images, self.width, self.height, w, h)

      
    def initialize_population(self):
        return [Individual(self.images, self.width, self.height) for _ in range(self.pop_size)] 

    def tournament_selection(self):
        selected = []
        for _ in range(self.pop_size // 2):
            tournament = random.sample(self.population, self.tournament_size)
            selected.append(max(tournament, key=lambda ind: ind.fitness))
        return selected

    def crossover(self, parent1, parent2, child1, child2):
        i = random.randint(1, self.n - 1)
        j = random.randint(self.n, 2 * self.n - 1)
        
        # Ukrstanje na oba dela hromozoma
        order1 = parent1.code[:i] + [k for k in parent2.code[:self.n] if k not in parent1.code[:i]]
        orijentations1 = parent1.code[self.n:j] + parent2.code[j:]
        child1.code = order1 + orijentations1

        order2 = [k for k in parent2.code[:self.n] if k not in child1.code[i:self.n]] + parent1.code[i:self.n]
        orijentations2 = parent2.code[self.n:j] + parent1.code[j:]
        child2.code = order2 + orijentations2

    def mutation(self, chromosome):
        for i in range(self.n):
          # Random broj za prvu polovinu niza
          if random.random() < self.mutation_prob:
                j = random.randint(0, self.n - 1)
                random.shuffle(chromosome.code[i:j])
          # Random broj za drugu polovinu niza
          if random.random() < self.mutation_prob:
              chromosome.code[self.n + i] = not chromosome.code[self.n + i]
    
    def run(self):
        new_population = deepcopy(self.population)
        for _ in range(self.num_generations):
            self.population.sort(key=lambda x: x.fitness, reverse=True)
            new_population[:self.elitism_size] = self.population[:self.elitism_size]
            for j in range(self.elitism_size, self.pop_size, 2):
                selection = self.tournament_selection()
                parent1, parent2 = random.sample(selection, 2)

                self.crossover(parent1, parent2, new_population[j-1], new_population[j])

                self.mutation(new_population[j-1])
                self.mutation(new_population[j])

            self.population = deepcopy(new_population)

            for ind in self.population:
                ind.update_fitness()

        # Get the best chromosome
        best = max(self.population, key=lambda x: x.fitness)
        
        print(best.fitness)
        self.show(best.code)
        return best
