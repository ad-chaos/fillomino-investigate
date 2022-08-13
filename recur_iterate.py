stack = [starting_node]
while len(stack):
    if kind_count > grid[starting_node]:
        break
    visiting_node = stack.pop()
    if grid[starting_node] == grid[visiting_node]:
        visited.add(node)
        kind_count += 1
    for node in graph[visiting_node]:
        stack.append(node)
        if grid[starting_node] == grid[node]:
            visited.add(node)
            kind_count += 1




for node in graph[starting_node]:
    if node in visited:
        continue
    if grid[starting_node] == grid[node]:
        visited.add(node)
        kind_count += 1
        dfs_impl(grid, node, visited, state)
