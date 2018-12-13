from math import inf
import numpy as np
import copy


class Node:
    def __init__(self, matrix, path, transition, parentPrice):
        self.matrix = matrix
        self.path = path
        self.transition = transition
        self.parentPrice = parentPrice
        self.price = parentPrice
        self.reduceRows()
        self.reduceCols()
        # print(self.matrix, 'asdf')

    def reduceRows(self):
        for i in range(1, len(self.matrix)):
            minVal = inf
            for j in range(1, len(self.matrix)):
                if self.matrix[i][j] < minVal:
                    minVal = self.matrix[i][j]
            if minVal != inf:
                self.price += minVal
            for j in range(1, len(self.matrix)):
                self.matrix[i][j] = inf if minVal == inf else self.matrix[i][j] - minVal

    def reduceCols(self):
        for i in range(1, len(self.matrix)):
            minVal = inf
            for j in range(1, len(self.matrix)):
                if self.matrix[j][i] < minVal:
                    minVal = self.matrix[j][i]
            if minVal != inf:
                self.price += minVal
            for j in range(1, len(self.matrix)):
                self.matrix[j][i] = inf if minVal == inf else self.matrix[j][i] - minVal
                # self.matrix[j][i] -= minVal

    def findMaxPricePosition(self):
        # print(self.matrix)
        maxTransition = []
        maxPrice = -1
        for i in range(1, len(self.matrix)):
            for j in range(1, len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    if len(self.matrix) > 2:
                        rowMin = min(np.delete(self.matrix[i, :], j)[1:])
                        colMin = min(np.delete(self.matrix[:, j], i)[1:])
                    else:
                        rowMin, colMin = 0, 0
                    curPrice = rowMin + colMin
                    if curPrice > maxPrice:
                        # print(i, j)
                        # print(self.matrix)
                        # print(rowMin, colMin)
                        # print(self.matrix[i, :][1:], self.matrix[:, j][1:])
                        # print(np.delete(self.matrix[i, :], j)[
                        #       1:], np.delete(self.matrix[:, j], i)[1:])
                        # print("Price: "+str(curPrice),
                        #       self.matrix[0], self.matrix[:, 0][i])
                        # print(self.matrix)
                        # maxTransition = [i, j, self.matrix[0][j]]
                        maxTransition = [int(self.matrix[:, 0][i]),
                                         int(self.matrix[0, :][j]), [i, j]]
                        maxPrice = curPrice
        # print(maxTransition, )
        return maxTransition

    def branch(self):
        maxTransition = self.findMaxPricePosition()
        result = []

        # print(maxTransition)
        # a) not transition
        tmpMatrix = copy.deepcopy(self.matrix)
        tmpMatrix[maxTransition[2][0]][maxTransition[2][1]] = inf
        result.append(Node(tmpMatrix,
                           self.path, [maxTransition[0],
                                       maxTransition[1], False],
                           self.price))
        # print('1', tmpMatrix)
        # b) not transition
        tmpMatrix = copy.deepcopy(self.matrix)
        tmpMatrix = np.delete(tmpMatrix, maxTransition[2][0], axis=0)
        tmpMatrix = np.delete(tmpMatrix, maxTransition[2][1], axis=1)
        if maxTransition[2][0] in tmpMatrix[:, 0] and maxTransition[2][1] in tmpMatrix[0][:]:
            # print('Max: ',maxTransition)
            tmpMatrix[maxTransition[2][1]][maxTransition[2][0]] = inf
        # print('2', tmpMatrix)
        # print(tmpMatrix[0][:], tmpMatrix[:, 0])
        # col = np.delete(self.matrix[:, i[1]][1:], i[0]-1)
        # row = np.delete(self.matrix[i[0]][1:], i[1]-1)
        # print(tmpMatrix)
        result.append(Node(tmpMatrix,
                           {maxTransition[0]: maxTransition[1], **self.path},
                           [maxTransition[0], maxTransition[1], True],
                           self.price))
        return result

    def __str__(self):
        # print(self.transitions)
        return str(self.transition) + " : " + str(self.price)+"/" \
            + str(self.parentPrice) + " - " + str(self.path)
