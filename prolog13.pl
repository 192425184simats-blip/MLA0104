% Facts
fever.
cough.

% Rule
flu :-
    fever,
    cough.

% Forward Chaining
diagnosis :-
    flu,
    write('Patient is suffering from Flu.').
