#Read/Write functions for Bicone algorithm
import numpy as np
import copy
import csv
import ast
from BiconeClasses import *

def data_writer(group, data):

    #Calculate frequencies used by AraSim, this is the only part of the GA that uses this
    freq_coeffs = round((data['maximum_frequency']-data['minimum_frequency']) / data['freq_step'] + 1)
    freq_array = []
    for i in range(freq_coeffs):
        freq_array.append(data['minimum_frequency'] + (data['freq_step'] * i))

    #Write Data to csv
    with open('generationDNA.csv', mode = 'w', newline='') as generationDNA:
        generationDNA.truncate()
        generation_writer = csv.writer(generationDNA, quoting=csv.QUOTE_NONNUMERIC)

        #Useless header for compatability with existing scripts
        for i in range(7):
            generation_writer.writerow("#")

        generation_writer.writerow(freq_array)
        generation_writer.writerow("#")
        for i in range(group.return_size()):
            generation_writer.writerow(group.return_chromosome(i))


def data_reader(CurrentGen):
    #Read in the genetic data
    chromosome_array = []
    with open('generationDNA.csv', newline='') as generationDNA:
        generation_reader = csv.reader(generationDNA, quoting=csv.QUOTE_NONNUMERIC)
        #for useless header
        for i in range(9):
            next(generationDNA)              #Skips the first 9 lines of the file
        for row in generation_reader:
            chromosome_array.append(row) 
    
    #Read in the fitness data
    fitness_array = []
    with open('fitnessScores.csv', newline = '') as fitnessScores:
        fitness_reader = csv.reader(fitnessScores, quoting=csv.QUOTE_NONNUMERIC)
        next(fitnessScores)              #Skips the first 2 lines of the file
        next(fitnessScores)
        for row in fitness_reader:
            fitness_array.append(row[0])

    for i in range(len(chromosome_array)):
        CurrentGen.add_individual(chromosome = chromosome_array[i], fitness = fitness_array[i])


        


            


