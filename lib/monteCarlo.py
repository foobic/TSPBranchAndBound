import math, random
from functions import *

def monteCarlo(matrix, res, iter=False):
    if iter == False:
        # iter = len(matrix) * 1000
        iter = math.pow(len(matrix), 5)
        # iter = math.pow(len(matrix), len(matrix))
    # iter = 0
    minVal = math.inf
    minPath = []
    while iter != 0:
    # while minVal != res:

        sequence = list([i+1 for i in range(0, len(matrix))])
        path = [] 
        while len(sequence) != 0 :
            val = random.choice(sequence)
            # indx = sequence.index(val)
            sequence.remove(val)
            path.append(val)
            # print(val,sequence)
            # print(, indx)
        path.append(path[0])
        newPathPrice = calcSum(matrix, path)
        # print(path, calcSum(matrix, path))
        if  newPathPrice < minVal:
            minVal = newPathPrice
            minPath = path
        # iter += 1
        iter -= 1
    
    # print(minPath, iter)
    print('Monte-Carlo: ', str(minPath), ' ', minVal, ' - ', len(matrix)*1000)