from math import factorial

from tqdm import tqdm

from utils import num_partitions_of
from utils import partitions

if __name__ == "__main__":
    count = 0
    n = 3  # side length of the grid
    m = 9  # the maximum sized polyomino allowed by the grid
    permutations_of_grid = factorial(n * n)

    for part in tqdm(partitions(n * n), total=(num_partitions_of(n * n))):
        if max(part) > m:
            continue
        grid = []
        for num in part:
            grid += [num for _ in range(num)]

        temp = permutations_of_grid
        for duplicate in part:
            temp /= factorial(duplicate)

        count += temp

    print("Total search space using partition idea:", count)
    print("Total search space using naive method:", m**n**2)
