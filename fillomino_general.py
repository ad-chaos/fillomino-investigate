from tqdm import tqdm
from itertools import product
from utils import is_valid_fillomino_game
from utils import graph3x3

if __name__ == "__main__":
    count = 0
    for game in tqdm(product(range(1,10), repeat=9), total=387420489):
        if is_valid_fillomino_game(game, graph3x3):
            count += 1

    print(f"Total Count: {count}")
