from queue import PriorityQueue

graph = {}

heuristic = {}

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("\nNode Name: ")

    h = int(input("Heuristic value: "))
    heuristic[node] = h

    m = int(input("Number of neighbours: "))

    neighbours = []

    for j in range(m):
        neighbour = input("Neighbour Name: ")
        neighbours.append(neighbour)

    graph[node] = neighbours


def greedy(start, goal):

    visited = []
    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    while not pq.empty():

        h, node = pq.get()

        if node not in visited:

            print(node, end=" ")

            visited.append(node)

            if node == goal:
                print("\nGoal Reached")
                return

            for neighbour in graph[node]:
                if neighbour not in visited:
                    pq.put((heuristic[neighbour], neighbour))


greedy(start, goal)
