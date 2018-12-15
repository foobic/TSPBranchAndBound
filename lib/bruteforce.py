import numpy as np
import itertools
import math
import random
import time




# matrix = np.array([[math.inf, 74., 30., 70., 84., 31., 26., 59.],
#                    [1., math.inf, 39., 98., 25., 57., 73., 33.],
#                    [39., 11., math.inf, 16., 56., 29., 91., 10.],
#                    [82., 65., 78., math.inf, 86., 74., 59., 97.],
#                    [28., 80., 41., 40., math.inf, 50., 91., 50.],
#                    [62.,  6., 49., 29., 79., math.inf, 82., 64.],
#                    [19., 29., 10., 26., 17., 10., math.inf, 25.],
#                    [13., 67., 62., 36., 49., 33., 65., math.inf]])


def bruteforce(matrix):
    startTime = time.time()

    allTransitions = []
    # matrix = np.array([
    #     [math.inf, 45, 61],
    #     [56, math.inf, 69],
    #     [14, 36, math.inf],
    # ])

    # matrix = generateRandomMatrix(8)

    # matrix = np.array([
    #     [math.inf, 20, 18, 12, 8],
    #     [5, math.inf, 14, 7, 11],
    #     [12, 18, math.inf, 6, 11],
    #     [11, 17, 11, math.inf, 12],
    #     [5, 5, 5, 5, math.inf],
    # ])

    matrixLen = len(matrix)

    # for i in matrix:
    #     print(i)

    entry = [*list(range(1, matrixLen+1)), 1]
    for i in list(itertools.permutations(entry)):
        if i[0] != 1 or i[len(i)-1] != 1 or i in allTransitions:
            continue
        allTransitions.append(i)
    # print(allTransitions, len(allTransitions))

    minPath = []
    minLen = math.inf
    for i in allTransitions:
        curLen = 0
        for j in range(1, matrixLen+1):
            curLen += matrix[i[j-1]-1][i[j]-1]
        if curLen < minLen:
            minPath = i[:]
            minLen = curLen

    return [minPath, minLen]
    print("Best Price: ", minLen)
    print("Best Path: ", minPath)
    # print("Time: ", time.time() - startTime)


