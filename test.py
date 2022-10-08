from pprint import pprint
from utils import bfs, gen_graph

outcomes = {True: "Passed ✅", False: "Failed ❌"}

graph0x0 = []

graph1x1 = [()]

graph2x2 = [
    (1, 2),
    (0, 3),
    (0, 3),
    (1, 2),
]

graph3x3 = [
    (1, 3),
    (0, 2, 4),
    (1, 5),
    (0, 6, 4),
    (1, 7, 3, 5),
    (2, 8, 4),
    (3, 7),
    (6, 8, 4),
    (7, 5),
]

graph4x4 = [
    (1, 4),
    (0, 5, 2),
    (1, 6, 3),
    (2, 7),
    (0, 5, 8),
    (1, 4, 6, 9),
    (5, 2, 10, 7),
    (3, 6, 11),
    (4, 9, 12),
    (8, 5, 13, 10),
    (9, 6, 14, 11),
    (15, 10, 7),
    (8, 13),
    (12, 9, 14),
    (13, 10, 15),
    (11, 14),
]

graph5x5 = [
    (1, 5),
    (0, 6, 2),
    (1, 7, 3),
    (2, 8, 4),
    (3, 9),
    (0, 6, 10),
    (1, 5, 11, 7),
    (6, 2, 12, 8),
    (7, 3, 13, 9),
    (4, 8, 14),
    (5, 11, 15),
    (10, 6, 16, 12),
    (11, 7, 17, 13),
    (12, 8, 18, 14),
    (9, 13, 19),
    (10, 16, 20),
    (15, 11, 21, 17),
    (16, 12, 22, 18),
    (17, 13, 23, 19),
    (14, 18, 24),
    (15, 21),
    (20, 16, 22),
    (21, 17, 23),
    (22, 18, 24),
    (19, 23),
]


def test_dfs3x3(grid, cases, truth):
    visited = set()
    grid_state = {}
    for test_node, truth in zip(cases, truth):
        if test_node in grid_state:
            print(outcomes[truth == grid_state[test_node]])
            continue

        visited.add(test_node)
        result = bfs(grid, test_node, visited, grid_state, graph3x3)
        print(outcomes[result == truth])


def test_dfs4x4(grid, cases, truth):
    visited = set()
    grid_state = {}
    for test_node, truth in zip(cases, truth):
        if test_node in grid_state:
            print(outcomes[truth == grid_state[test_node]])
            continue

        visited.add(test_node)
        result = bfs(grid, test_node, visited, grid_state, graph4x4)
        print(outcomes[result == truth])
        for node in visited:
            grid_state[node] = result


def test_grid_equality(
    generated: list[tuple[int, ...]], expected: list[tuple[int, ...]]
):
    final_result = True
    for i, j in zip(generated, expected):
        final_result &= sorted(i) == sorted(j)

    return final_result


# tests

print("Testing Grid Graph Generator: ")
print(outcomes[test_grid_equality(gen_graph(0), graph0x0)])
print(outcomes[test_grid_equality(gen_graph(1), graph1x1)])
print(outcomes[test_grid_equality(gen_graph(3), graph3x3)])
print(outcomes[test_grid_equality(gen_graph(4), graph4x4)])
print(outcomes[test_grid_equality(gen_graph(5), graph5x5)])
print()

print("Testing Grid 1: ")
grid = [2, 5, 5, 2, 5, 2, 5, 5, 2]
test_dfs3x3(grid, [0, 1, 8], [True, True, True])
print()

print("Testing Grid 2: ")
grid = [7, 2, 7, 7, 2, 7, 7, 7, 7]
test_dfs3x3(grid, [0, 1], [True, True])
print()

print("Testing Grid 3: ")
grid = [4, 4, 6, 4, 4, 6, 6, 6, 6]
test_dfs3x3(grid, [1, 3], [True, True])
print()

print("Testing Grid 4: ")
grid = [6, 1, 6, 6, 6, 6, 1, 6, 1]
test_dfs3x3(grid, [1, 4, 6, 8], [True, True, True, True])
print()

print("Testing Grid 5: ")
grid = [8, 8, 8, 8, 8, 8, 8, 8, 1]
test_dfs3x3(grid, [1, 8], [True, True])
print()

print("Testing Grid 6: ")
grid = [9, 9, 9, 9, 9, 9, 9, 9, 9]
test_dfs3x3(grid, [1, 4, 7], [True, True, True])
print()

print("Testing Grid 7: ")
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_dfs3x3(grid, [0, 2, 4, 8], [True, False, False, False])
print()

print("Testing Grid 8: ")
grid = [1, 1, 1, 1, 1, 1, 1, 1, 1]
test_dfs3x3(grid, [0, 2, 4, 8], [False, False, False, False])
print()


print("Testing Grid 9: ")
grid = [1, 1, 2, 2, 5, 5, 5, 5, 5]
test_dfs3x3(grid, [0, 2], [False, False])
print()

print("Testing Grid 10: ")
grid = [4, 4, 3, 3, 4, 4, 3, 1, 2, 2, 6, 6, 6, 6, 6, 6]
"""
4 4 3 3
4 4 3 1
2 2 6 6
6 6 6 6
"""
# breakpoint()
test_dfs4x4(grid, [0, 3, 6, 1], [True, True, True, True])
print()

print("Testing Grid 11: ")
grid = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_dfs4x4(grid, [1, 5, 9], [False, False, False])
print()

# print("Testing Grid 12: ")
# grid = [6, 6, 6, 6, 5, 6, 5, 6, 5, 5, 5, 2, 2, 1, 1, 1]
# test_dfs4x4(grid, [11, 15, 0, 5, 12, 13], [False, False, True, True, False, False])
# print()
