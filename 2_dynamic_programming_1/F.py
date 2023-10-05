def dfs(graph, water_height, node=0, visited=None):
    # check the graph is connected or not by depth-first search
    if visited is None:
        visited = set()
    visited.add(node)

    for neighbor, way_height in enumerate(graph[node]):
        if neighbor not in visited and way_height > water_height:
            dfs(graph, water_height, neighbor, visited)

    return len(graph) == len(visited)


def binary_search(graph, heights):
    # for sorted list of unique heights = [h_0, h_1, ..., h_n] there is a list of connectivity indicators
    # [1, ..., 1, 0, ..., 0] (inverse sorted list) for which need to find x := the first left zero,
    # invariant: if dfs(graph, m) == 1 --> x in (m, r], else x in (l, m]
    left, right = -1, len(heights) - 1
    while right - left > 1:

        mid = (left + right) // 2  # m is always equal to or greater than 0
        if dfs(graph, water_height=heights[mid]):
            left = mid
        else:
            right = mid

    return heights[right]


num_houses, num_ways = map(int, input().split())
graph = [[0] * num_houses for _ in range(num_houses)]
heights = set()

for _ in range(num_ways):
    i, j, height = map(int, input().split())
    graph[i - 1][j - 1] = graph[j - 1][i - 1] = height
    heights.add(height)

heights = sorted(heights)
print(binary_search(graph, heights))


