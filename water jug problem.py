from collections import deque

def solve(cap1, cap2, cap3, target1, target2):
    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b, c), path = queue.popleft()

        if (a, b, c) in visited:
            continue

        visited.add((a, b, c))
        path = path + [(a, b, c)]

        # Check goal
        if a == target1 and b == target2:
            print("\nSolution Found:\n")
            for i, state in enumerate(path):
                print(f"Step {i}: Jug1={state[0]}L, Jug2={state[1]}L, Jug3={state[2]}L")
            return

        next_states = []

        # Fill
        next_states += [
            (cap1, b, c),
            (a, cap2, c),
            (a, b, cap3)
        ]

        # Empty
        next_states += [
            (0, b, c),
            (a, 0, c),
            (a, b, 0)
        ]

        # Pour J1->J2
        t = min(a, cap2 - b)
        next_states.append((a - t, b + t, c))

        # Pour J1->J3
        t = min(a, cap3 - c)
        next_states.append((a - t, b, c + t))

        # Pour J2->J1
        t = min(b, cap1 - a)
        next_states.append((a + t, b - t, c))

        # Pour J2->J3
        t = min(b, cap3 - c)
        next_states.append((a, b - t, c + t))

        # Pour J3->J1
        t = min(c, cap1 - a)
        next_states.append((a + t, b, c - t))

        # Pour J3->J2
        t = min(c, cap2 - b)
        next_states.append((a, b + t, c - t))

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("No solution exists.")


# -------- Main --------

cap1 = int(input("Enter capacity of Jug 1: "))
cap2 = int(input("Enter capacity of Jug 2: "))
cap3 = int(input("Enter capacity of Jug 3: "))

target1 = int(input("Required water in Jug 1: "))
target2 = int(input("Required water in Jug 2: "))

solve(cap1, cap2, cap3, target1, target2)
