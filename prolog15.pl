% Food items
food(apple).
food(vegetable).
food(peanuts).

% John likes all kinds of food
likes(john, X) :-
    food(X).

% John likes peanuts
likes(john, peanuts).

% Harry eats everything that Anil likes
eats(harry, X) :-
    likes(anil, X).

% Anil likes peanuts
likes(anil, peanuts).

% Anil eats peanuts and is alive
eats(anil, peanuts).
alive(anil).

% Anything anyone eats and is not killed is food
food(X) :-
    eats(_, X),
    \+ killed(X).

% Nothing is killed (default)
killed(_) :- fail.
