from tqdm import tqdm
from itertools import product
from utils import bfs, graph3x3

# https://stackoverflow.com/a/44209393
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p

def is_valid(grid: tuple[int]) -> bool:
    is_valid = True
    visited = set()
    grid_state = {}
    for sourcenode in graph3x3.keys():
        if sourcenode in visited:
            continue
        visited.add(sourcenode)
        is_valid &= bfs(grid, sourcenode, visited, grid_state, graph3x3)
        if not is_valid:
            return False

    return True

if __name__ == "__main__":
    count = 0
    for game in tqdm(product(range(1,10), repeat=9), total=387420489):
        if is_valid(game):
            count += 1

    print(f"Total Count: {count}")
