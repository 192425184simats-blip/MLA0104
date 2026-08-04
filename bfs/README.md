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
