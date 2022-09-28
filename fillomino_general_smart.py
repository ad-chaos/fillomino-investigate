import sys
from itertools import product
from typing import Dict

from more_itertools import distinct_permutations
from tqdm import tqdm

from utils import bfs
from utils import graphs
from utils import num_partitions_of

# https://stackoverflow.com/a/44209393
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p


def is_valid(grid: tuple[int], graphnxn: Dict[int, tuple[int, ...]]) -> bool:
    is_valid = True
    visited = set()
    grid_state = {}
    for sourcenode in graphnxn.keys():
        if sourcenode in visited:
            continue
        visited.add(sourcenode)
        is_valid &= bfs(grid, sourcenode, visited, grid_state, graphnxn)

    return is_valid


if __name__ == "__main__":
    count = 0
    n = 3  # side length of the grid
    m = 9  # the maximum sized polyomino allowed by the grid
    graph_chosen = graphs[n]

    # If S_p(a) generates all the partitions of number `a`
    # and Permute(S) gives the permutation for every
    # ordered pair in the list S
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
            if is_valid(game, graph_chosen):
                print(f"{grid[0]} {grid[1]} {grid[2]}\n{grid[3]} {grid[4]} {grid[5]}\n{grid[6]} {grid[7]} {grid[8]}\n\n")
                count += 1

    print("Total Count: ", count)
