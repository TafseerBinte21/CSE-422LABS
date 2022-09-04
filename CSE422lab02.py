from re import A
from typing import Tuple
from typing import List, Tuple
import random


# generate random chorosomes and form a population
def getPopulation(population):

    for i in range(population):
        binary = []
        for j in range(total_players):
            rand = random.randint(0, 1)
            binary.append(rand)

        total_population.append(binary)


# calculate fitness values for all the chromosomes in the population
def fitness(population):
    fitness_list = []
    for i in range(len(population)):
        fitness_calculation = 0
        sum = 0
        for j in range(len(population[i])):
            if population[i][j] == 1:
                sum += players_arr[j][1]

        diff = m - sum
        if diff < 0:
            fitness_calculation = m + diff
        else:
            fitness_calculation = m - diff
        population[i] = (population[i], fitness_calculation)
        fitness_list.append(fitness_calculation)
        
    return fitness_list
   

def selection(population, weights):
    return random.choices(population=population, weights=weights)[0]


def crossover(chromosome1, chromosome2):
    r = random.randint(0, len(chromosome1) - 1)
    child = chromosome1[0: r] + chromosome2[r:]
    return child


def mutation(chromosome):
    mutation_threshold = 0.3 
    _index1 = random.randrange(len(chromosome))
    _index2 = random.randrange(len(chromosome))

    if (random.random() > mutation_threshold):
        random_index1_value = chromosome[_index1]
        chromosome[_index1] = chromosome[_index2]
        chromosome[_index2] = random_index1_value
    return chromosome


def genetic(total_population):
    gen = 0
    while True:
        # print("Generation", gen, ":", total_population, "\n")
        fitness_value = fitness(total_population)

        sorted_population = sorted(total_population, key=lambda x: x[1])
        # print("\n", sorted_population)

        if sorted_population[-1][1] == m:
            return sorted_population[-1][0]

        new_population = [sorted_population[-1][0], sorted_population[-2][0]]
        # print(new_population)

        for i in range(len(total_population)-2):
            chromosome1 = selection(total_population, fitness_value)[0]
            chromosome2 = selection(total_population, fitness_value)[0]

            crossed = crossover(chromosome1, chromosome2)
            while crossed == [0 for x in range(total_players)]:
                crossed = crossover(chromosome1, chromosome2)
            mutated = mutation(crossed)
            new_population.append(mutated)
        total_population = new_population
        gen += 1


with open('input2.txt') as inFile:
    A = inFile.readline().split()
    n = int(A[0])
    m = int(A[1])
    array = []
    for j in range(n):
        se = inFile.readline().strip()

        array.append(se)
    
total_players = n
# print(total_players)

players_arr: List[Tuple[int, int]] = []
players =  []

for i in range(total_players):
    player_names, player_avgruns = array[i].split(" ")
    players_arr.append((player_names, int(player_avgruns)))
    players.append((player_names))
    

print(players)
# print(players_arr)
binary = []
total_population = []
# population  = 10



getPopulation(10)
# print(total_population)
# print()

answer = genetic(total_population)
if answer == -1:
    print("-1")
else:
    for i in range(len(answer)):
        if i== len(answer)-1:
            print(answer[i])
        else:
            print(answer[i],end=" ")
# print(*answer,sep=" ")

