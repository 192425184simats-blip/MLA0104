% Best First Search (Simple Example)

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

best_first(a, Goal) :-
    search(a, Goal).

search(Node, Node) :-
    write('Goal Found: '),
    writeln(Node).

search(Node, Goal) :-
    edge(Node, Next),
    search(Next, Goal).
