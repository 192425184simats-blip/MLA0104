from collections import deque

start = (1,2,3,
         4,0,6,
         7,5,8)

goal = (1,2,3,
        4,5,6,
        7,8,0)

moves = {
0:[1,3],
1:[0,2,4],
2:[1,5],
3:[0,4,6],
4:[1,3,5,7],
5:[2,4,8],
6:[3,7],
7:[4,6,8],
8:[5,7]
}

queue=deque()
queue.append((start,0))
visited=set()

while queue:

    state,depth=queue.popleft()

    if state==goal:
        print("Solved")
        print("Moves =",depth)
        break

    if state in visited:
        continue

    visited.add(state)

    zero=state.index(0)

    for move in moves[zero]:
        new=list(state)
        new[zero],new[move]=new[move],new[zero]
        queue.append((tuple(new),depth+1))
