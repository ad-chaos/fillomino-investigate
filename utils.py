from typing import Dict, Set

graph0x0 = {}

graph1x1 = {0: (0,)}

graph2x2 = {
    0: (1, 2),
    1: (0, 3),
    2: (0, 3),
    3: (1, 2),
}

graph3x3 = {
    0: (1, 3),
    1: (0, 2, 4),
    2: (1, 5),
    3: (0, 6, 4),
    4: (1, 7, 3, 5),
    5: (2, 8, 4),
    6: (3, 7),
    7: (6, 8, 4),
    8: (7, 5),
}

graph4x4 = {
    0: (1, 4),
    1: (0, 5, 2),
    2: (1, 6, 3),
    3: (2, 7),
    4: (0, 5, 8),
    5: (1, 4, 6, 9),
    6: (5, 2, 10, 7),
    7: (3, 6, 11),
    8: (4, 9, 12),
    9: (8, 5, 13, 10),
    10: (9, 6, 14, 11),
    11: (15, 10, 7),
    12: (8, 13),
    13: (12, 9, 14),
    14: (13, 10, 15),
    15: (11, 14),
}


graph5x5 = {
    0: (1, 5),
    1: (0, 6, 2),
    2: (1, 7, 3),
    3: (2, 8, 4),
    4: (3, 9),
    5: (0, 6, 10),
    6: (1, 5, 11, 7),
    7: (6, 2, 12, 8),
    8: (7, 3, 13, 9),
    9: (4, 8, 14),
    10: (5, 11, 15),
    11: (10, 6, 16, 12),
    12: (11, 7, 17, 13),
    13: (12, 8, 18, 14),
    14: (9, 13, 19),
    15: (10, 16, 20),
    16: (15, 11, 21, 17),
    17: (16, 12, 22, 18),
    18: (17, 13, 23, 19),
    19: (14, 18, 24),
    20: (15, 21),
    21: (20, 16, 22),
    22: (21, 17, 23),
    23: (22, 18, 24),
    24: (19, 23),
}
graphs = [graph0x0, graph1x1, graph2x2, graph3x3, graph4x4, graph5x5]


def bfs(
    grid: tuple[int, ...],
    starting_node: int,
    visited: Set[int],
    grid_state: Dict[int, bool],
    graph: Dict[int, tuple[int, ...]],
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
    grid: tuple[int, ...], graphnxn: Dict[int, tuple[int, ...]]
) -> bool:
    is_valid = True
    visited = set()
    grid_state = {}
    for sourcenode in graphnxn.keys():
        if sourcenode in visited:
            continue
        visited.add(sourcenode)
        is_valid &= bfs(grid, sourcenode, visited, grid_state, graphnxn)
    return is_valid
