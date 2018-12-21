from lib.BranchAndBound import BranchAndBound
from lib.bruteforce import bruteforce
from math import inf
from functions import *
import random
import sys

#BnB - Branch and bound method

def testBnB(size, matrix=False, printResult=False):
    if not matrix: 
        matrix = generateRandomMatrix(size)
    res = BranchAndBound(matrix).start(printResult)
    check = calcSum(matrix, res[0])
    if check != res[1]:
        print("Err")
        sys.exit()
    else:
        print("BnB Test successfully passed")


def testBnBandBruteforce(size, matrix=False, printResult=False):
    # compares results for random matrix BnB and Bruteforce
    if not matrix: 
        if size > 9:
            print('Bruteforcing very slow, therefore you can`t use it for size > 9 ')
            sys.exit()
        matrix = generateRandomMatrix(size)
    res1 = BranchAndBound(matrix).start()
    res2 = bruteforce(matrix)
    if res1[1] != res2[1]:
        print("Err")
        print('BnB: ', res1, calcSum(matrix, res1[0]))
        print('Bruteforce: ', res2, calcSum(matrix, res2[0]))
        for i in matrix:
            print(i)
        sys.exit()
    if printResult:
        print('----')
        print('BnB: ', res1, calcSum(matrix, res1[0]))
        print('Bruteforce: ', res2, calcSum(matrix, res2[0]))
        for i in matrix:
            print(i)
        return calcSum(matrix, res2[0])
    else:
        print("BnBandBruteforce Test successfully passed")
