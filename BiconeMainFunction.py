#Bicone algorithm python edition written by Ben Sipe *
import os
import sys
import numpy as np

from BiconeClasses import *
from BiconeDataManipulator import *
from BiconeOperators import *
from BiconeSelectionMethods import *

data = {'tournament_ratio' : 0.5,       #Ratio of prior generation that undergoes tournament selection
        'roulette_ratio' : 0.5,
        'population' : 10,
        'pool_size' : 3,                #Amount of competitors in one round of tournament

        #Operator ratios
        'mutation_ratio' : 0.1 ,        #Ratio of population that is mutated
        'reproduction_ratio' : 0.2,     #Ratio of population to be cloned
        'crossover_ratio' : 0.7,        #Ratio of population that is crossed over

        #Antenna size constraints
        'min_length' : 37.5,       #in cm
        'max_length' : 140.0,      #in cm
        'min_radius' : 0.0,        #in cm
        'max_radius' : 7.5,        #in cm
        'min_angle' : 0.0,         #in radians
        'max_angle' : 0.197,       #in radians

        #AraSim constants
        'minimum_frequency' : 0.08333,  #Minimum frequency we're working in (GHZ)
        'maximum_frequency' : 1.0667,   #Max frequency in GHZ
        'freq_step' : 0.01667,          #Step size between frequencies
        }


#Start of the GA
if sys.argv[1] == 'start':

    FirstGen = Group(group_size = data['population'])
    FirstGen.generate_new_group(data)

    data_writer(FirstGen, data)

#After generating the initial population
if sys.argv[1] == 'cont':

    current_gen = Group()
    data_reader(current_gen)

    #Run Selection Methods on current_gen and put winners into winner_group
    winner_group = Group()
    tournament(current_gen, winner_group, data)
    roulette(current_gen, winner_group, data)


    #Run operators on winner_group and put new individuals into offspring
    offspring = Group()
    crossover(winner_group, offspring, data)
    mutation(winner_group, offspring, data)
    reproduction(winner_group, offspring, data)

    #write offspring genetic data to csv
    data_writer(offspring, data)





