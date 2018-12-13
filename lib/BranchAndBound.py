import numpy as np
from treelib import Node, Tree
from math import inf
from .Node import Node
# TODO
# - add sys.time() for time measurement


class BranchAndBound:
    def __init__(self, matrix):
        self.tree = Tree()
        node = Node(np.array(self.createIndexes(matrix)), {}, [], 0)
        self.tree.create_node(str(node), hash(node), data=node)  # root node
        self.leafs = {hash(node): hash(node)}
        # self.resultPath = {}
        self.matrixLen = len(matrix)

    def createIndexes(self, matrix):
        newMatrix = [list([inf, *list([i+1 for i in range(0, len(matrix))])])]
        for i in range(0, len(matrix)):
            newMatrix.append([i+1, *matrix[i]])
        return newMatrix

    def showTree(self):
        # if self.tree.size() > 60:
        #     return
        print("\n\n*** Tree Output ***")
        self.tree.show(line_type="ascii-exr")
        print("*** End Tree Output ***\n\n")

    def findMinPriceLeaf(self):
        minPrice = inf
        minLeafHash = 0
        for i in self.leafs:
            curLeaf = self.tree.get_node(i)
            # print(curLeaf.data.price)
            if len(curLeaf.data.path) == self.matrixLen:
                return self.tree[i].data  # stop
            if curLeaf.data.price < minPrice:
                minPrice = curLeaf.data.price
                minLeafHash = i
            # print(,'11')

        del self.leafs[minLeafHash]
        # print(minLeafHash, 2)
        return minLeafHash

    def printResult(self, resultNode):
        D = resultNode.path
        current = 1
        path = [current]
        while D:
            current = D.pop(current)
            path.append(current)
        print('Path: ', " → ".join(str(i) for i in path))

    def start(self):
        print('===============')
        # self.showTree()
        # print(self.leafs)
        # for i in self.leafs:
        #     print(i)

        while True:
            print('='*100)
            minPriceNodeHash = self.findMinPriceLeaf()
            print(minPriceNodeHash, type(minPriceNodeHash))
            if isinstance(minPriceNodeHash, Node):
                self.printResult(minPriceNodeHash)
                break
            minPriceNode = self.tree[minPriceNodeHash]
            newSubNodes = minPriceNode.data.branch()
            self.leafs[hash(newSubNodes[0])] = hash(newSubNodes[0])
            self.leafs[hash(newSubNodes[1])] = hash(newSubNodes[1])
            self.tree.create_node(str(newSubNodes[0]),
                                  hash(newSubNodes[0]),
                                  data=newSubNodes[0],
                                  parent=minPriceNode.identifier)
            self.tree.create_node(str(newSubNodes[1]),
                                  hash(newSubNodes[1]),
                                  data=newSubNodes[1],
                                  parent=minPriceNode.identifier)

            # self.showTree()
            # break

        self.showTree()
        # print()
#
        # print(self.resultPath, len(self.resultPath))
        # print(self.tree.all_nodes())
