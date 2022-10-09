import sys

from more_itertools import distinct_permutations
from tqdm import tqdm

from utils import gen_graph
from utils import print_grid
from utils import num_partitions_of
from utils import partitions
from utils import is_valid_fillomino_game


def max_n(parts: tuple[tuple[int, ...]]) -> int:
    max_num = -1
    for part in parts:
        for num in part:
            max_num = max(num, max_num)
    return max_num


def fillomino_finder_smart(side_length, max_size):

    # If S_p(a) generates all the partitions of number `a`
    # and Permute(S) gives all the permutations of the tuple S
    # then our search space is Permute(S_p(n*n))
    # if the max_size is less than n*n then we ignore partitions where any
    # number inside it is greater than max_size

    all_games = []
    grid_graph = gen_graph(side_length)
    for part in tqdm(
        partitions(side_length * side_length),
        total=(num_partitions_of(side_length * side_length)),
    ):
        if max(part) > max_size:
            continue

        grid = []
        for num in part:
            grid += [num for _ in range(num)]

        for game in distinct_permutations(grid):
            if is_valid_fillomino_game(game, grid_graph, side_length):
                all_games.append(game)

    return all_games


if __name__ == "__main__":
    # Takes two inputs if run as python fillomino_general_smart.py <n> <m>
    # n: side length of the grid
    # m: the maximum sized polyomino allowed by the grid
    n, m = map(int, sys.argv[1:]) if len(sys.argv) == 3 else (3, 9)
    games = fillomino_finder_smart(n, m)
    print(f"Total games possible are:", len(games))
    for game in games:
        print_grid(game, n)
