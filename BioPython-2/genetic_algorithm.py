# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 05:45:37 2019

@author: Yujin Yoshimura
CMPS 4553 Survey Computational Methods
Dr. Tina Johnson
Program 6

This program implements genetic algorithm with fitness-proportionate selection,
roulette-wheel sampling, single-point crossover, and bitwise mutation.
"""

import random

"""
header
@param: file
@return: void
Writes header into the output file.
"""
def header(outf):
    name = 'Yujin Yoshimura'
    course = 'CMPS 4553 Survey Computational Methods'
    instructor = 'Dr. Tina Johnson'
    iteration = 'Program 6'
    description = 'This program implements genetic algorithm with fitness-proportionate selection,\n'
    description += 'roulette-wheel sampling, single-point crossover, and bitwise mutation.\n'
    
    outf.write(name + '\n')
    outf.write(course + '\n')
    outf.write(instructor + '\n')
    outf.write(iteration + '\n')
    outf.write('\n')
    outf.write(description + '\n')
    outf.write('\n')

"""
initialize
@param: int, int
@return: list of list of int (population)
Randomly generates chromosomes of 0s and 1s.
"""
def initialize(population, length):
    p = []
    for ch in range(population):
        chromosome = []
        for gene in range(length):
            chromosome.append(random.randrange(2))
        p.append(chromosome)
    return p

"""
fitness
@param: list of int (chromosome)
@return: int
Counts number of genes matched in a given chromosome.
"""
def fitness(ch):
    f = 0
    for gene in ch:
        if gene == 1:
            f += 1
    return f

"""
select
@param: list of list of int (population)
@return: list of int (chromosome)
Selects random chromosome weighted by fitness.
"""
def select(p):
    total = 0
    subtotals = [0]
    for ch in p:
        total += fitness(ch)
        subtotals.append(total)
    selected = random.randrange(total)
    for i in range(len(subtotals) - 1):
        if selected >= subtotals[i]:
            chosen = i
    return(p[chosen])

"""
crossover
@param: list of int (chromosome), list of int (chromosome)
@return: list of int (chromosome)
Generates new chromosome from two given chromosomes.
"""
def crossover(ch1, ch2):
    point = random.randrange(len(ch1))
    offspring = []
    for i in range(len(ch1)):
        if i <= point:
            offspring.append(ch1[i])
        else:
            offspring.append(ch2[i])
    return(offspring)

"""
mutate
@param: list of int (chromosome)
@return: list of int (chromosome)
Mutates new chromosome from a given chromosome.
"""
def mutate(ch):
    point1 = random.randrange(len(ch))
    point2 = random.randrange(len(ch))
    if point1 > point2:
        point1, point2 = point2, point1
    offspring = []
    for i in range(len(ch)):
        if i < point1:
            offspring.append(ch[i])
        elif i <= point2:
            offspring.append(1 - ch[i])
        else:
            offspring.append(ch[i])
    return(offspring)

"""
iterate
@param: list of list of int (population), int, int
@return: list of list of int (population)
Creates new set of chromosomes from given population.
"""
def iterate(p, pc, pm):
    new_p = []
    for i in range(len(p)):
        r = random.uniform(0, 1)
        if r < pm:
            new_p.append(mutate(select(p)))
        elif r < pc + pm:
            new_p.append(crossover(select(p), select(p)))
        else:
            new_p.append(select(p))
    return new_p

"""
print_fitness
@param: file, int, list of list of int (population),
@return: list of list of int (population)
Creates new set of chromosomes from given population.
"""
def print_fitness(outf, generation, p):
    total = 0
    max = 0
    for ch in p:
        total += fitness(ch)
        if max < fitness(ch):
            max = fitness(ch)
    ave = total / len(p)
    outf.write('{0: >10}'.format(str(generation)) + '{0: >18}'.format(str(ave)) + ' ' + '{0: >14}'.format(str(max)) + '\n')

"""
main
@param: void
@return: void
Main function.
"""
def main():
    population = 100
    length = 20
    pc = 0.7
    pm = 0.001
    p = initialize(population, length)
    with open("genetic_algorithm.txt", "w", encoding = "utf8") as outf:
        header(outf)
        outf.write('Population size : ' + str(population) + '\n')
        outf.write('Genome length   : ' + str(length) + '\n')
        outf.write('Crossover rate  : Pc = ' + str(pc) + '\n')        
        outf.write('Mutation rate   : Pm = ' + str(pm) + '\n')        
        outf.write('\nGeneration   Average Fitness   Best Fitness\n')
        for generation in range(20):
            print_fitness(outf, generation, p)
            p = iterate(p, pc, pm)
        print_fitness(outf, 20, p)

if __name__ == '__main__':
    main()