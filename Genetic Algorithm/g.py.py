import random

population = []
genome = []

# Initializing population
def initialize(popSize, geneSize):
    for i in range(popSize):
        x = random.randint(0,15)
        y = random.randint(0,15)
        x = bin(x)[2:].zfill(geneSize)
        y = bin(y)[2:].zfill(geneSize)
        x_y = [int(digit) for digit in str(x)] + [int(digit) for digit in str(y)]
        population.append(x_y)



# Evaluating function for 3x+2y = 50
def evaluate(x,y):
    y_pred = 3 * x + 2 * y
    fitness = 50 - y_pred
    print(" ")
    print("Predicted Value: ", y_pred)
    print("Current Error: ", fitness)

    # Convergence check
    if( 2 >= fitness >= -2 ):
       print()
       print('---------Good-Fit---------')
       print("------Solution found------")
       print(f"3*{x}+2*{y}={y_pred}")
       print("Solution: ", y_pred)
       print("Error: ", fitness)
       quit()



# Sorting population based upon fitness
def sort_population():
    errors = []
    for pop in population:
        x = pop[:geneSize]
        y = pop[geneSize:]
        x = int(''.join(map(str, x)), 2)
        y = int(''.join(map(str, y)), 2)
        errors.append(evaluate(x,y))
    sort_fitness(errors, population)

# Sorting population accordingly with fitness rank
def sort_fitness(array1, array2):
    zipped_pairs = list(zip(array1, array2))
    zipped_pairs.sort()
    sorted_array1, sorted_array2 = zip(*zipped_pairs)
    errors = list(sorted_array1)
    global population 
    population = list(sorted_array2)


def pair_population():
    if populationSize>1:
        popPair = []
        global population
        # CrossOver
        for i in range(len(population)-1):
            popPair.append(population[i])
            popPair.append(population[i+1])
        # Mutation
        for i in range(0, len(popPair)-1, 2):

            index = random.randint(0, geneSize)
            popPair[i][index], popPair[i+1][index] = popPair[i+1][index], popPair[i][index]
# Generating Next Generation and populating array
        population = popPair[:populationSize]




# Main Program------------------------------------------------
geneSize = 8
populationSize = 10
iteration = 0
loop = 0

initialize(populationSize, geneSize)

while(True):
    print(" ")
    print("Generation: ",iteration)
    iteration = iteration+1
    sort_population()
    pair_population()
    if(loop>100):
        population = []
        genome = []
        initialize(populationSize,geneSize)
        loop=0
    loop = loop+1


