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
