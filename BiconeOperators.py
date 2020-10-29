#Operators for Bicone algorithm
import random
import sys
import copy
import numpy as np
from BiconeClasses import Group, Individual

def crossover(winner_group, offspring, data):
    winner_group = copy.deepcopy(winner_group)
    crossover_runs = round(data['crossover_ratio'] * winner_group.return_size()/2)
    if crossover_runs == 0:
       sys.exit('crossover ratio not high enough or population is too small')

    for i in range(crossover_runs):
        selected_gene = random.randrange(winner_group.return_number_of_genes())
        print(selected_gene)
        parent1 = winner_group.return_chromosome(2*i)
        parent2 = winner_group.return_chromosome(2*i+1)

        parent1_new = np.append(parent1[:selected_gene], parent2[selected_gene:])
        parent2_new = np.append(parent2[:selected_gene], parent1[selected_gene:])

        offspring.add_individual(parent1_new,0)
        offspring.add_individual(parent2_new,0)


def mutation(winner_group, offspring, data):
    winner_group = copy.deepcopy(winner_group)
    crossover_runs = round(data['crossover_ratio'] * winner_group.return_size()/2)
    mutation_runs = round(data['mutation_ratio'] * winner_group.return_size())

    for i in range(mutation_runs):
        x = random.randint(0, winner_group.return_number_of_genes()-1)
        print(i+crossover_runs*2)
        mutated_chromosome = winner_group.gene_mutator(individual = (i+crossover_runs*2), gene = x, data = data)

        offspring.add_individual(mutated_chromosome, 0)

def reproduction(winner_group, offspring, data):
    winner_group = copy.deepcopy(winner_group)
    crossover_runs = round(data['crossover_ratio'] * winner_group.return_size()/2)
    mutation_runs = round(data['mutation_ratio'] * winner_group.return_size())
    reproduction_runs = winner_group.return_size() - crossover_runs*2 - mutation_runs
    
    for i in range(reproduction_runs):
        offspring.add_individual(winner_group.return_chromosome(i + mutation_runs + crossover_runs*2),0)