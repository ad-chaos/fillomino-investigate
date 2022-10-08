import sys
from tqdm import tqdm
from itertools import product

from utils import gen_graph, print_grid
from utils import is_valid_fillomino_game


def fillomino_finder_naive(side_length, max_size):
    all_games = []
    count = 0
    graphnxn = gen_graph(side_length)
    for game in tqdm(product(range(1, max_size+1), repeat=side_length*side_length), total=max_size**(side_length*side_length)):
        if is_valid_fillomino_game(game, graphnxn ,side_length):
            all_games.append(game)
            print_grid(game, side_length)
            count += 1

    print(f"Total Count: {count}")
    return all_games

if __name__=="__main__":
    fillomino_finder_naive(*map(int, sys.argv[1:]) if len(sys.argv) == 3 else (3, 9))
