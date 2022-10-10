from math import factorial
from collections import Counter

from utils import partitions


def searchspace(n, m):
    count = 0
    permutations_of_grid = factorial(n * n)

    for part in partitions(n * n):
        if max(part) > m:
            continue

        temp = permutations_of_grid
        for duplicate in Counter(num for num in part for _ in range(num)).values():
            temp /= factorial(duplicate)

        count += temp

    return int(count), m**n**2


if __name__ == "__main__":
    # Going over the searchspace when we have some ixi grid
    # Stopped at 8x8 because after that the integers become _quite_ large
    for i in range(9):
        smart, naive = searchspace(i, i*i)
        print("Search-Space for a %dx%d grid"%(i,i))
        print("Partitions:", smart)
        print("Naive Method:", naive)
        print()
