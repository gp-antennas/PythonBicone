#Selection Methods for Bicone algorithm
import random
import numpy as np
from BiconeClasses import *

def tournament(group, winner_group, data):
    tournament_runs = round(data['tournament_ratio'] * group.return_size())
    for i in range(tournament_runs):
        chosen_index = random.sample(range(0, group.return_size()), data['pool_size'])
        winner = chosen_index[0]
        for index in chosen_index:
            if group.return_fitness(index) > group.return_fitness(winner):
                winner = index

        winner_group.add_individual(group.return_chromosome(winner),group.return_fitness(winner))


def roulette(group, winner_group, data):
    roulette_runs = round(data['roulette_ratio'] * group.return_size())
    total = 0.0

    for individual in range(group.return_size()):
        total = total + group.return_fitness(individual)
    for i in range(roulette_runs):
        pick = random.uniform(0.0, total)
        current = 0.0
        for individual in range(group.return_size()):
            current += group.return_fitness(individual)
            if current > pick:
                winner_group.add_individual(group.return_chromosome(individual),group.return_fitness(individual))
                break

            

            
        


    