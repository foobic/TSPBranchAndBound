from math import inf
import random

def generateRandomMatrix(size, maxNumber=100):
    matrix = []
    for i in range(0, size):
        tmp = []
        for j in range(0, size):
            if i != j:
                tmp.append(random.randint(0, maxNumber))
            else:
                tmp.append(inf)
        matrix.append(tmp)
    return matrix

def calcSum(matrix, transitions):
    res = 0
    for i in range(1, len(transitions)):
        res += matrix[transitions[i-1]-1][transitions[i]-1]
    return res