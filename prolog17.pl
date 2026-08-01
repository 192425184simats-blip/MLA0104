% Marcus was a man
man(marcus).

% Marcus was a Pompeian
pompeian(marcus).

% All Pompeians were Romans
roman(X) :-
    pompeian(X).

% Caesar was a ruler
ruler(caesar).

% All Romans were either loyal to Caesar or hated Caesar
loyal(X, caesar) :-
    roman(X),
    \+ hates(X, caesar).

hates(X, caesar) :-
    roman(X),
    \+ loyal(X, caesar).

% Everyone is loyal to someone
loyal(X, someone) :-
    person(X).

% People only try to assassinate rulers they are not loyal to
not_loyal(X, Y) :-
    person(X),
    ruler(Y),
    tried_to_assassinate(X, Y).

% If a person is not loyal to a ruler, then he hates that ruler
hates(X, Y) :-
    not_loyal(X, Y).

% Marcus tried to assassinate Caesar
tried_to_assassinate(marcus, caesar).

% All men are people
person(X) :-
    man(X).
