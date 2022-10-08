import sys
from math import factorial

from tqdm import tqdm

from utils import num_partitions_of
from utils import partitions

if __name__ == "__main__":
    count = 0
    n, m = map(int, sys.argv[1:]) if len(sys.argv) == 3 else (3, 9)
    permutations_of_grid = factorial(n * n)

    for part in partitions(n * n):
        if max(part) > m:
            continue
        grid = []
        for num in part:
            grid += [num for _ in range(num)]

        temp = permutations_of_grid
        for duplicate in part:
            temp /= factorial(duplicate)

        count += temp

    print("Total search space using partition idea:", int(count))
    print("Total search space using naive method:", m**n**2)
