#Classes for Bicone Algorithm
import numpy as np
import random

class Individual:

    def __init__(self, chromosome = None, fitness = 0.0):
        self.fitness = fitness                    #Fitness Score of the Individual
        if chromosome is None:                    #Genetic material for the Individual
            self.chromosome = []
        else:
            self.chromosome = chromosome

    #THESE FUNCTIONS PASS VALUES TO THE GROUP CLASS
    def pass_chromosome(self):
        return(self.chromosome)

    def pass_fitness(self):
        return self.fitness

    #INITIAL GENERATION CHROMOSOME GENERATOR
    def generate_chromosome(self, data):
        radius_1 = random.uniform(data['min_radius'],data['max_radius'])
        length_1 = random.uniform(data['min_length'], data['max_length'])
        angle_1 = random.uniform(data['min_angle'], data['max_angle'])
        radius_2 = random.uniform(data['min_radius'],data['max_radius'])
        length_2 = random.uniform(data['min_length'], data['max_length'])
        angle_2 = random.uniform(data['min_angle'], data['max_angle'])
        
        self.chromosome = [radius_1, length_1, angle_1, radius_2, length_2, angle_2]
        


#This describes a generation which is an object that is an array of Individuals as defined above
class Group:

    def __init__(self, individual_array = None, group_size = 0, number_of_genes = 6):
        self.group_size =  group_size                #This is the number of individuals in a group or generation
        if individual_array is None:
            self.individual_array = []               #This is the array that contains arrays of chromosomes     
        self.number_of_genes = number_of_genes       #For asymmetric bicone this is 6: r_1,l_1,a_1,r_2,l_2,a_2

    #CREATE FIRST GENERATION
    def generate_new_group(self,dict): 
        for i in range(self.group_size):
            individual = Individual()
            individual.generate_chromosome(dict)
            self.individual_array.append(individual)
    
    #CREATE GROUPS FOR SUBSEQUENT GENERATIONS
    def add_individual(self, chromosome, fitness):
        individual = Individual(chromosome = chromosome, fitness = fitness)
        self.individual_array.append(individual)
        self.group_size += 1

    #DATA RETURNS
    def return_size(self):
        return self.group_size

    def return_number_of_genes(self):
        return(self.number_of_genes)

    def return_fitness(self,individual):
        return(self.individual_array[individual].pass_fitness())

    def return_chromosome(self, individual):
        return(self.individual_array[individual].pass_chromosome())

    def print_all(self):
        for i in range(self.group_size):
            print(self.return_chromosome(i))

    #USED IN THE MUTATION OPERATOR
    def gene_mutator(self, individual, gene, data):
        chromosome = self.individual_array[individual].pass_chromosome()
        radius_1 = random.uniform(data['min_radius'],data['max_radius'])
        length_1 = random.uniform(data['min_length'], data['max_length'])
        angle_1 = random.uniform(data['min_angle'], data['max_angle'])
        radius_2 = random.uniform(data['min_radius'],data['max_radius'])
        length_2 = random.uniform(data['min_length'], data['max_length'])
        angle_2 = random.uniform(data['min_angle'], data['max_angle'])
        choice_array = [radius_1, length_1, angle_1, radius_2, length_2, angle_2]

        chromosome[gene] = choice_array[gene]
        return chromosome



        

        





        
            

        





        

       
