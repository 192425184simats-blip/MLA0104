from collections import deque

capacity = (11,9)
goal = 8

visited = set()

queue = deque()
queue.append(((0,0),[]))

while queue:

    (a,b),path = queue.popleft()

    if a==goal or b==goal:
        print("Solution Found")
        for step in path:
            print(step)
        print("Final State =", (a,b))
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    next_states=[]

    next_states.append(((11,b),"Fill Jug1"))
    next_states.append(((a,9),"Fill Jug2"))

    next_states.append(((0,b),"Empty Jug1"))
    next_states.append(((a,0),"Empty Jug2"))

    transfer=min(a,9-b)
    next_states.append(((a-transfer,b+transfer),"Pour Jug1->Jug2"))

    transfer=min(b,11-a)
    next_states.append(((a+transfer,b-transfer),"Pour Jug2->Jug1"))

    for state,action in next_states:
        if state not in visited:
            queue.append((state,path+[action]))
