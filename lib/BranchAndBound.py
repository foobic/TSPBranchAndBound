import numpy as np
import time
from treelib import Node, Tree
from math import inf
from .Node import Node

class BranchAndBound:
    def __init__(self, matrix):
        self.tree = Tree()
        node = Node(np.array(matrix), 0, 0,  0, {})
        self.tree.create_node(str(node), hash(node), data=node)  # root node
        self.leafs = {hash(node): hash(node)}
        self.matrixLen = len(matrix)

    def findMinCostLeaf(self):
        minCost = inf
        minLeafHash = 0
        for i in self.leafs:
            curLeaf = self.tree.get_node(i)
            if curLeaf.data.cost < minCost:
                minCost = curLeaf.data.cost
                minLeafHash = i
        del self.leafs[minLeafHash]
        return minLeafHash

    def getResult(self, resultNode):
        D = resultNode.path
        current = 0
        path = [current]
        while D:
            current = D.pop(current)
            path.append(current)
        return [tuple([i+1 for i in path]), resultNode.cost]

    def start(self, printResult=False):
        startTime = time.time()
        minLeafHash, minLeaf = None, None
        while True:
            minLeafHash = self.findMinCostLeaf()
            minLeaf = self.tree[minLeafHash]
            if self.tree.level(minLeafHash) == self.matrixLen:
                break
            matrices = minLeaf.data.branch()
            for i in matrices:
                iHash = hash(i)
                self.tree.create_node(
                    str(i), iHash, parent=minLeafHash, data=i)
                self.leafs.update({iHash: iHash})
        res = self.getResult(minLeaf.data)
        
        if printResult:
            print('===============')
            print('Cost: ', res[1])
            print('Path: ', " → ".join(str(i) for i in res[0]))
            print("End time(BnB): ", time.time() - startTime)
            # self.tree.show(line_type="ascii-exr") # show tree
        return  res
        # self.showTree()
