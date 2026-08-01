from collections import deque

maze = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 'G']
]

rows = len(maze)
cols = len(maze[0])

# Directions: Down, Up, Right, Left
directions = [(1,0), (-1,0), (0,1), (0,-1)]

queue = deque()
visited = set()

# (row, col, path)
queue.append((0, 0, [(0,0)]))

while queue:
    x, y, path = queue.popleft()

    if maze[x][y] == 'G':
        print("Goal Reached!")
        print("Shortest Path:")
        for p in path:
            print(p)
        print("Total Cost (Steps):", len(path)-1)
        break

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if (0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] != 1 and
            (nx, ny) not in visited):

            queue.append((nx, ny, path + [(nx, ny)]))
