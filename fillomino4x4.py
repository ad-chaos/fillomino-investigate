from more_itertools import distinct_permutations
from itertools import product
from utils import dfs, graph4x4
from tqdm import tqdm


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
    for sourcenode in graph4x4.keys():
        if sourcenode in visited:
            continue
        visited.add(sourcenode)
        is_valid &= dfs(grid, sourcenode, visited, grid_state, graph4x4)
        if not is_valid:
            return False

    return True


if __name__ == "__main__":
    count = 0
    for p9, p7 in tqdm(product(partitions(9), partitions(7)), total=30 * 15):
        grid = []
        for num9 in p9:
            grid += [num9 for _ in range(num9)]
        for num7 in p7:
            grid += [num7 for _ in range(num7)]

        for game in distinct_permutations(grid):
            if is_valid(game):
                count += 1

    print(f"Total Count: {count}")
