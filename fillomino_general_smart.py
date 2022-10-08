from itertools import product
import sys

from more_itertools import distinct_permutations
from tqdm import tqdm

from utils import gen_graph
from utils import print_grid
from utils import num_partitions_of
from utils import partitions
from utils import is_valid_fillomino_game

count = 0
# n: side length of the grid
# m: the maximum sized polyomino allowed by the grid
n, m = map(int, sys.argv[1:]) if len(sys.argv) == 3 else (3, 9)

# If S_p(a) generates all the partitions of number `a`
# and Permute(S) gives all the permutations of the tuple S
# then our search space is Permute(S_p(m)^q * S_p(r))
# where m,q and r are integers that satisfy the equation
# n^2 = mq + r { 0<= r < m }

q = n * n // m
r = n * n - m * q

partition_iterators = [partitions(m) for _ in range(q)]
if r:
    partition_iterators += [partitions(r)]

for parts in tqdm(
    product(*partition_iterators),
    total=(num_partitions_of(m) ** q) * num_partitions_of(r),
):
    grid = []
    for part in parts:
        for num in part:
            grid += [num for _ in range(num)]

    for game in distinct_permutations(grid):
        if is_valid_fillomino_game(game, gen_graph(n), n):
            print_grid(game, n)
            count += 1

print("Total Count: ", count)
