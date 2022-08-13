import sys
from math import factorial
from collections import Counter
from itertools import product
from utils import partitions_of
from tqdm import tqdm

# https://stackoverflow.com/a/44209393
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p


if __name__ == "__main__":
    count = 0
    n = int(sys.argv[1])  # side length of the grid
    m = 9  # the maximum sized polyomino allowed by the grid
    naive_space = factorial(n * n)

    q = n * n // m
    r = n * n - m * q

    partition_iterators = [partitions(m) for _ in range(q)]
    if r:
        partition_iterators += [partitions(r)]

    for parts in tqdm(
        product(*partition_iterators), total=(partitions_of(m) ** q) * partitions_of(r)
    ):
        grid = []
        for part in parts:
            for num in part:
                grid += [num for _ in range(num)]

        temp = naive_space
        for duplicate in Counter(grid).keys():
            temp /= factorial(duplicate)
            print(f"Had to search through {temp} permutations of the grid")

        count += temp
        #count += len(tuple(distinct_permutations(grid)))

    print(f"Total search space: {count}")
