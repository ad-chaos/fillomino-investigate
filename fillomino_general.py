import sys
from tqdm import tqdm
from itertools import product

from utils import gen_graph, print_grid
from utils import is_valid_fillomino_game


def fillomino_finder_naive(side_length, max_size):
    all_games = []
    graphnxn = gen_graph(side_length)
    for game in tqdm(
        product(range(1, max_size + 1), repeat=side_length * side_length),
        total=max_size**side_length**2,
    ):
        if is_valid_fillomino_game(game, graphnxn, side_length):
            all_games.append(game)

    return all_games


if __name__ == "__main__":
    n, m = map(int, sys.argv[1:]) if len(sys.argv) == 3 else (3, 9)
    games = fillomino_finder_naive(n, m)
    print(f"Total games possible are:", len(games))
    for game in games:
        print_grid(game, n)
