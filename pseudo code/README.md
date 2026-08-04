#BFS
CREATE empty Queue Q
CREATE empty set Visited

ENQUEUE StartNode into Q
ADD StartNode to Visited

WHILE Q is not empty DO
    Node ← DEQUEUE Q
    VISIT Node

    FOR each Neighbor of Node in Graph DO
        IF Neighbor not in Visited THEN
            ADD Neighbor to Visited
            ENQUEUE Neighbor into Q
        END IF
    END FOR
END WHILE

#DFS
CREATE empty set Visited

CALL DFS_Visit(StartNode)

DFS_Visit(Node)

    ADD Node to Visited
    VISIT Node

    FOR each Neighbor of Node in Graph DO
        IF Neighbor not in Visited THEN
            CALL DFS_Visit(Neighbor)
        END IF
    END FOR

END DFS_Visit

#UCS
CREATE PriorityQueue PQ
INSERT (StartNode, Cost = 0) into PQ

CREATE empty set Visited

WHILE PQ not empty DO
    Node ← REMOVE node with lowest cost from PQ

    IF Node is Goal THEN
        RETURN path and cost
    END IF

    IF Node not in Visited THEN
        ADD Node to Visited

        FOR each Neighbor of Node DO
            NewCost ← Cost(Node) + Cost(Node → Neighbor)

            INSERT (Neighbor, NewCost) into PQ
        END FOR
    END IF
END WHILE

#WATER-JUG
DEFINE initial state (x, y)

CREATE Queue Q
CREATE set Visited

ENQUEUE initial state into Q

WHILE Q not empty DO
    (x, y) ← DEQUEUE Q

    IF (x, y) is Goal State THEN
        PRINT solution
        STOP
    END IF

    GENERATE possible states:
        Fill Jug X
        Fill Jug Y
        Empty Jug X
        Empty Jug Y
        Pour X → Y
        Pour Y → X

    FOR each new state DO
        IF state not in Visited THEN
            ADD state to Visited
            ENQUEUE state
        END IF
    END FOR
END WHILE

A*SEARCH 
CREATE PriorityQueue OPEN
CREATE set CLOSED

INSERT StartNode into OPEN
SET f(Start) = g(Start) + h(Start)

WHILE OPEN not empty DO

    Node ← node with lowest f(n) from OPEN

    IF Node is Goal THEN
        RETURN path
    END IF

    MOVE Node from OPEN to CLOSED

    FOR each Neighbor of Node DO

        IF Neighbor in CLOSED THEN
            CONTINUE
        END IF

        g_new = g(Node) + cost(Node → Neighbor)
        f_new = g_new + h(Neighbor)

        IF Neighbor not in OPEN OR g_new is smaller THEN
            UPDATE Neighbor cost
            INSERT Neighbor into OPEN
        END IF

    END FOR
END WHILE

GBFS
CREATE PriorityQueue OPEN
INSERT StartNode into OPEN

CREATE set Visited

WHILE OPEN not empty DO

    Node ← node with smallest heuristic h(n)

    IF Node is Goal THEN
        RETURN path
    END IF

    ADD Node to Visited

    FOR each Neighbor of Node DO
        IF Neighbor not in Visited THEN
            INSERT Neighbor into OPEN
        END IF
    END FOR

END WHILE

MINI-MAX
FUNCTION Minimax(Node, Depth, IsMax)

IF Node is leaf OR Depth = 0 THEN
    RETURN value(Node)
END IF

IF IsMax = TRUE THEN
    Best ← -∞

    FOR each Child of Node DO
        Value ← Minimax(Child, Depth-1, FALSE)
        Best ← MAX(Best, Value)
    END FOR

    RETURN Best

ELSE
    Best ← +∞

    FOR each Child of Node DO
        Value ← Minimax(Child, Depth-1, TRUE)
        Best ← MIN(Best, Value)
    END FOR

    RETURN Best
END IF
