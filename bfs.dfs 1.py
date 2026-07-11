from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


n = int(input("Enter number of nodes: "))

graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter connected nodes: ").split()
    graph[node] = neighbours


start = input("Enter starting node: ")

print("BFS:", bfs(graph, start))
print("DFS:", dfs(graph, start))
