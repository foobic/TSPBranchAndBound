from lib.BranchAndBound import BranchAndBound
from math import inf

BranchAndBound(
    [
        [inf, 7, 9, 2],
        [5, inf, 4, 7],
        [6, 4, inf, 3],
        [9, 2, 7, inf],
    ]
).start()
# BranchAndBound(
#     [
#         [inf, 10, 2, 27],
#         [4, inf, 3, 13],
#         [5, 3, inf, 25],
#         [7, 5, 9, inf],
#     ]).start()
# ).start()

# test(7, 25, )

# BranchAndBound(
#     [
#         [inf, 45, 61],
#         [56, inf, 69],
#         [14, 36, inf],
#     ]
# ).start()
