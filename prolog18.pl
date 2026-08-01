% Facts
fever.
cough.
body_pain.

% Rule
flu :-
    fever,
    cough,
    body_pain.

% Forward Chaining
forward :-
    flu,
    write('Diagnosis: Patient has Flu.').
