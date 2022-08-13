from utils import dfs, graph3x3, graph4x4


def test_dfs3x3(grid, cases, truth):
    visited = set()
    grid_state = {}
    for test_node, true in zip(cases, truth):
        visited.add(test_node)
        if true:
            assert dfs(grid, test_node, visited, grid_state, graph3x3)
        else:
            assert not dfs(grid, test_node, visited, grid_state, graph3x3)


def test_dfs4x4(grid, cases, truth):
    visited = set()
    grid_state = {}
    for test_node, true in zip(cases, truth):
        visited.add(test_node)
        if true:
            assert dfs(grid, test_node, visited, grid_state, graph4x4)
        else:
            assert not dfs(grid, test_node, visited, grid_state, graph4x4)


# tests
grid = [2, 5, 5, 2, 5, 2, 5, 5, 2]
test_dfs3x3(grid, [0, 1, 8], [True, True, True])

grid = [7, 2, 7, 7, 2, 7, 7, 7, 7]
test_dfs3x3(grid, [0, 1], [True, True])

grid = [4, 4, 6, 4, 4, 6, 6, 6, 6]
test_dfs3x3(grid, [1, 3], [True, True])

grid = [6, 1, 6, 6, 6, 6, 1, 6, 1]
test_dfs3x3(grid, [1, 4, 6, 8], [True, True, True, True])

grid = [8, 8, 8, 8, 8, 8, 8, 8, 1]
test_dfs3x3(grid, [1, 8], [True, True])

grid = [9, 9, 9, 9, 9, 9, 9, 9, 9]
test_dfs3x3(grid, [1, 4, 7], [True, True, True])

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_dfs3x3(grid, [0, 2, 4, 8], [True, False, False, False])

grid = [1, 1, 1, 1, 1, 1, 1, 1, 1]
test_dfs3x3(grid, [0, 2, 4, 8], [False, False, False, False])

grid = [4, 4, 3, 3, 4, 4, 3, 1, 2, 2, 6, 6, 6, 6, 6, 6]
test_dfs4x4(grid, [0, 3, 6, 1], [True, True, True, True])

grid = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_dfs4x4(grid, [1,5,9], [False, False, False])
