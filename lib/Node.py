from math import inf
import copy

class Node:
    def __init__(self, matrix,  vertexNum, parentVertexNum, parentCost, parentPath):
        self.matrix = copy.deepcopy(matrix)
        self.vertexNum = vertexNum
        self.parentVertexNum = parentVertexNum
        self.cost = parentCost
        self.parentCost = parentCost
        self.setInfinities(parentVertexNum, vertexNum)
        self.reduceMatrix()
        self.path = {**parentPath, parentVertexNum: vertexNum}

    def reduceMatrix(self):
        self.reduceRows()
        self.reduceCols()

    def setInfinities(self, from_, to):
        if from_ == to:
            return
        # recalc cost
        self.cost += self.matrix[from_][to]
        # setting infinity for reverse path
        self.matrix[to][from_] = inf
        # setting infinities to `to` row and `from_` column
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if i == from_ or j == to:
                    self.matrix[i][j] = inf

    def reduceRows(self):
        for i in range(0, len(self.matrix)):
            minVal = inf
            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] < minVal:
                    minVal = self.matrix[i][j]
            if minVal != inf:
                self.cost += minVal
            for j in range(0, len(self.matrix)):
                self.matrix[i][j] = inf if minVal == inf else self.matrix[i][j] - minVal

    def reduceCols(self):
        for i in range(0, len(self.matrix)):
            minVal = inf
            for j in range(0, len(self.matrix)):
                if self.matrix[j][i] < minVal:
                    minVal = self.matrix[j][i]
            if minVal != inf:
                self.cost += minVal
            for j in range(0, len(self.matrix)):
                self.matrix[j][i] = inf if minVal == inf else self.matrix[j][i] - minVal

    def branch(self):
        vertex = self.matrix[self.vertexNum]
        vertexFiltered = []
        for i in range(0, len(vertex)):
            if vertex[i] != inf:
                vertexFiltered.append([i, vertex[i]])
        newLeafs = []
        for i in vertexFiltered:
            newLeafs.append(Node(
                self.matrix, i[0], self.vertexNum, self.cost, self.path))
        return newLeafs

    def __str__(self):
        return str(self.parentVertexNum) + " : " \
            + str(self.vertexNum) + " : " + \
            str(self.cost) + " | " + str(self.path)
