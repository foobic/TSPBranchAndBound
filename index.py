from lib.BranchAndBound import BranchAndBound
from lib.bruteforce import bruteforce
from math import inf
from functions import *
from tests import *

# Laba
matrix = [
    [inf, 20, 30, 10, 11, 8],
    [15, inf, 16, 4, 2, 4],
    [3, 5, inf, 2, 4, 7],
    [19, 6, 18, inf, 3, 1],
    [16, 4, 7, 16, inf, 3],
    [1, 8, 3, 10, 4, inf],
]
testBnB(6, matrix, True)
# testBnBandBruteforce(6, matrix, True)


# Own matrix
# matrix = [
#     [inf, 20, 30, 10, 11],
#     [15, inf, 16, 4, 2],
#     [3, 5, inf, 2, 4],
#     [19, 6, 18, inf, 3],
#     [16, 4, 7, 16, inf],
# ]
# testBnB(5, matrix, True)
# testBnBandBruteforce(5, matrix, True)


# Random matrix
# testBnB(6, False, True)
# testBnBandBruteforce(6, False, True)


# for i in range(0, 100):
#     testBnBandBruteforce(6)
# for i in range(0, 100):
#     testBnB(6)


# testBnB(8, [
#     [inf, 74, 30, 70, 84, 31, 26, 59],
#     [1, inf, 39, 98, 25, 57, 73, 33],
#     [39, 11, inf, 16, 56, 29, 91, 10],
#     [82, 65, 78, inf, 86, 74, 59, 97],
#     [28, 80, 40, 40, inf, 50, 91, 50],
#     [62, 6, 49, 29, 79, inf, 82, 64],
#     [19, 29, 10, 26, 17, 10, inf, 25],
#     [13, 67, 62, 36, 49, 33, 65, inf],
# ], True)
