import numpy as np
import operator
import pandas as pd
import random


class Client:
    def __init__(self, state):
        self.state = state

    def distance(self, client, start):
        distance = abs(self.state[0]-client.state[0])+abs(self.state[1]-client.state[1])+  abs(
            self.state[0] - start.state[0]) + abs(self.state[1] - start.state[1])
        return distance

    def __repr__(self):
        return "(" + str(self.state[0]) + "," + str(self.state[1]) + ")"


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self, start):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromClient = self.route[i]
                toClient = None
                if i + 1 < len(self.route):
                    toClient = self.route[i + 1]
                else:
                    toClient = self.route[0]
                pathDistance += fromClient.distance(toClient, start)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self, start):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance(start))
        return self.fitness


def createRoute(clientList):
    route = []
    route.append(clientList[0])
    r = random.sample(clientList, len(clientList))
    for i in range(0, len(r)):
        if r[i] != route[0]:
            route.append(r[i])
    return route


def initialClients(clientsize, clientList):
    clientsr = []
    for i in range(0, clientsize):
        clientsr.append(createRoute(clientList))
    return clientsr


def rankRoutes(clientsr, start):
    fitnessResult = {}
    for i in range(0, len(clientsr)):
        fitness = Fitness(clientsr[i])
        fitnessResult[i] = fitness.routeFitness(start)
    return sorted(fitnessResult.items(), key=operator.itemgetter(1), reverse=True)


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(clients, selectionResults):
    matingPool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingPool.append(clients[index])
    return matingPool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]
    child = childP1 + childP2
    return child


def breedClients(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            client1 = individual[swapped]
            client2 = individual[swapWith]

            individual[swapped] = client2
            individual[swapWith] = client1
    return individual


def mutateClients(clients, mutationRate):
    mutatedPop = []

    for ind in range(0, len(clients)):
        mutatedInd = mutate(clients[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGen(currentGen, eliteSize, mutationRate, start):
    popRanked = rankRoutes(currentGen,start)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedClients(matingpool, eliteSize)
    nextGeneration = mutateClients(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, start, clientsize, eliteSize, mutationRate, generations):
    pop = initialClients(clientsize, population)

    for i in range(0, generations):
        pop = nextGen(pop, eliteSize, mutationRate, start)

    bestRouteIndex = rankRoutes(pop, start)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute
