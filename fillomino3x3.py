from itertools import product
from utils import dfs, graph3x3
from more_itertools import distinct_permutations

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
        is_valid &= dfs(grid, sourcenode, visited, grid_state, graph3x3)
        if not is_valid:
            return False

    return True


if __name__ == "__main__":
    count = 0
    for p in partitions(9):
        grid = []
        for num in p:
            grid += [num for _ in range(num)]

        for game in distinct_permutations(grid):
            if is_valid(game):
                print(game)
                count += 1

    print(f"Total Count: {count}")
