% Facts
fever.
cough.

% Rule
flu :-
    fever,
    cough.

% Backward Chaining
diagnose :-
    flu,
    write('Diagnosis: Patient has Flu.').
