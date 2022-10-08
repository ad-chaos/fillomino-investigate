from itertools import product

from more_itertools import distinct_permutations
from tqdm import tqdm

from utils import graphs
from utils import num_partitions_of
from utils import partitions
from utils import is_valid_fillomino_game

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
            if is_valid_fillomino_game(game, graph_chosen):
                print(f"{game[0]} {game[1]} {game[2]}\n{game[3]} {game[4]} {game[5]}\n{game[6]} {game[7]} {game[8]}\n\n")
                count += 1

    print("Total Count: ", count)
