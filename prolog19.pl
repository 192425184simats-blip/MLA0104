% Facts
fever.
cough.
body_pain.

% Rule
flu :-
    fever,
    cough,
    body_pain.

% Backward Chaining
backward :-
    flu,
    write('Diagnosis: Patient has Flu.').
