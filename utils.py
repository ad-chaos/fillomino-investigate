from typing import Dict, Set


def gen_graph(n: int) -> list[tuple[int, ...]]:
    grid_graph = []
    neighbours = []
    for i in range(n):
        for j in range(n):
            neighbours.clear()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + dx < n and 0 <= j + dy < n:
                    neighbours.append(n * (i + dx) + (j + dy))
            grid_graph.append(tuple(neighbours))

    return grid_graph


def bfs(
    grid: tuple[int, ...],
    starting_node: int,
    visited: Set[int],
    grid_state: Dict[int, bool],
    graph: list[tuple[int, ...]],
) -> bool:
    kind_count = 1
    stack = [starting_node]
    local_visited = set()
    while len(stack):
        visiting_node = stack.pop()

        for node in graph[visiting_node]:
            if node in visited:
                continue

            if grid[starting_node] == grid[node]:
                stack = [node] + stack  # stack.append(node)
                local_visited.add(node)
                visited.add(node)
                kind_count += 1

    a_polyomino = kind_count == grid[starting_node]

    for node in local_visited:
        grid_state[node] = a_polyomino

    return a_polyomino


# Code to just get the number of partitions of a number
# faster than generating tuples
def num_partitions_of(n):
    if n == 0:
        return 1
    S = 0
    J = n - 1
    k = 2
    while 0 <= J:
        T = num_partitions_of(J)
        S = S + T if (k // 2) % 2 else S - T
        J -= k if (k) % 2 else k // 2
        k += 1
    return S


# https://stackoverflow.com/a/44209393
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p


def is_valid_fillomino_game(
    grid: tuple[int, ...], graphnxn: list[tuple[int, ...]], side_lenght: int
) -> bool:
    is_valid = True
    visited = set()
    grid_state = {}
    for sourcenode in range(side_lenght**2):
        if sourcenode in visited:
            continue
        visited.add(sourcenode)
        is_valid &= bfs(grid, sourcenode, visited, grid_state, graphnxn)
    return is_valid


def print_grid(grid: tuple[int, ...], side_lenght: int) -> None:
    for i in range(side_lenght**2):
        if i % side_lenght == 0:
            print()
        print(grid[i], end=" ")
    print()
