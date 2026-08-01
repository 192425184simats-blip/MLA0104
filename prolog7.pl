% Male members
male(john).
male(david).
male(michael).
male(robert).

% Female members
female(mary).
female(linda).
female(susan).
female(anna).

% Parent relationships
parent(john, david).
parent(mary, david).

parent(john, susan).
parent(mary, susan).

parent(david, michael).
parent(linda, michael).

parent(david, anna).
parent(linda, anna).

% Rules
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandfather(X, Y) :-
    father(X, Z),
    parent(Z, Y).

grandmother(X, Y) :-
    mother(X, Z),
    parent(Z, Y).

brother(X, Y) :-
    male(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.
