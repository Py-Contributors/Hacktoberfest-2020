'''
code for 0/1 knapsack problem using Genetic Algorithm
'''

from random import choice
from itertools import cycle


class Point:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def desc(self):
        print(self.name, '     ', self.weight, '     ', self.value)


A = Point('A', 45, 3)
B = Point('B', 40, 5)
C = Point('C', 50, 8)
D = Point('D', 90, 10)

max_cap = 100
pop_size = 4

seq = [A, B, C, D]
dic = {'A': A, 'B': B, 'C': C, 'D': D}
num_points = len(seq)


def calc_value(chromosome):
    weight = sum([seq[index].weight*int(i) for index, i in enumerate(chromosome)])
    value = sum([seq[index].value*int(i) for index, i in enumerate(chromosome)])
    return weight, value


def fit_sort(population):
    fittest = []
    for chromosome in population:
        weight, value = calc_value(chromosome)
        if weight > max_cap:
            value = 0
        fittest.append(value)
    population = [x for _, x in sorted(zip(fittest, population), reverse=True)]
    return population


def cross(population):
    third = population[2]
    fourth = population[3]
    offsprings = [third[:2]+fourth[2:], fourth[:2]+third[2:]]
    return offsprings


def mutate(chromosome, element):
    index = seq.index(dic.get(element))
    gene = str(abs(int(chromosome[index]) - 1))
    chromosome[index] = gene
    return chromosome

iterations = 10
population = ['1111', '1000', '1010', '1001']
population = [list(string) for string in population]
cycle = cycle(['D', 'C', 'B', 'A'])
for i in range(iterations):
    fit = fit_sort(population)
    offsprings = cross(fit)
    changed = mutate(offsprings[0], next(cycle))
    offsprings[0] = changed
    population = fit[:2]+offsprings

population = fit_sort(population)
ans = population[0]
print(ans)
chosen = [point[0] for point in zip(seq, ans) if point[1]=='1']
total_weight, total_value = 0, 0

print('object', 'weight', 'value')
for point in chosen:
    total_weight += point.weight
    total_value += point.value
    point.desc()
print('total weight -> ', total_weight)
print('total value -> ', total_value)
