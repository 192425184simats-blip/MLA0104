%-------------------------
% FACTS
%-------------------------

% Marcus was a man
man(marcus).

% Marcus was a Pompeian
pompeian(marcus).

% Caesar was a ruler
ruler(caesar).

% Marcus tried to assassinate Caesar
assassinate(marcus, caesar).

%-------------------------
% RULES (Workflow)
%-------------------------

% All Pompeians were Romans
roman(X) :-
    pompeian(X).

% All Romans are people
person(X) :-
    roman(X).

% All men are people
person(X) :-
    man(X).

% People only try to assassinate rulers they are not loyal to
not_loyal(X,Y) :-
    person(X),
    ruler(Y),
    assassinate(X,Y).

% If a person is not loyal, then he hates that person
hates(X,Y) :-
    not_loyal(X,Y).

% A person is loyal only if he is not proved to be not loyal
loyal(X,Y) :-
    person(X),
    ruler(Y),
    \+ not_loyal(X,Y).
