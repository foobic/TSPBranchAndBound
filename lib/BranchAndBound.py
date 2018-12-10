import numpy as np
from treelib import Node, Tree
from math import inf
# TODO
# - add sys.time() for time measurement


class BranchAndBound:
    def __init__(self, matrix):
        
        self.matrix = np.array(self.createIndexes(matrix))

    def createIndexes(self, matrix):
        newMatrix = [list([inf, *list([i for i in range(0, len(matrix))])])]
        for i in range(0, len(matrix)):
            newMatrix.append([i, *matrix[i]])
        return newMatrix

    def start(self):
        print(self.matrix)
