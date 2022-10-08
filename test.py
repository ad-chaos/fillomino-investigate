from utils import bfs, graph3x3, graph4x4

outcomes = {True: "Passed ✅", False: "Failed ❌"}


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


# tests
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
test_dfs4x4(grid, [0, 3, 6, 1], [True, True, True, True])
print()

print("Testing Grid 11: ")
grid = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_dfs4x4(grid, [1, 5, 9], [False, False, False])
print()
