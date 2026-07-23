import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    visited = {}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, cost

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        for neighbor, weight in graph[current]:
            heapq.heappush(priority_queue,
                           (cost + weight, neighbor, path + [neighbor]))

    return None, float("inf")


# -------- Input --------
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("\nEnter node: ")
    m = int(input("Enter number of neighbours: "))

    neighbours = []
    for j in range(m):
        neighbour = input("Enter neighbour: ")
        cost = int(input("Enter cost: "))
        neighbours.append((neighbour, cost))

    graph[node] = neighbours

start = input("\nEnter source node: ")
goal = input("Enter goal node: ")

path, total_cost = uniform_cost_search(graph, start, goal)

if path:
    print("\nLeast Cost Path:", " -> ".join(path))
    print("Total Cost:", total_cost)
else:
    print("No path exists.")
