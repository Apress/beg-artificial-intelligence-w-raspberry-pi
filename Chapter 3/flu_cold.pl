%Flu or cold identification example
%Start with ?- go.

go:- hypothesis(Disease),
    write('I believe you have: '),
    write(Disease),
    nl,
    undo.

%Hypothesis that should be tested
hypothesis(cold):- cold, !.
hypothesis(flu):- flu, !.

%Hypothesis Identification Rules
cold :-
       verify(headache),
       verify(runny_nose),
       verify(sneezing),
       verify(sore_throat).
flu :-
       verify(fever),
       verify(headache),
       verify(chills),
       verify(body_ache).

/* how to ask questions */
ask(Question) :-
    write('Does the patient have the following symptom: '),
    write(Question),
    write('? '),
    read(Response),
    nl,
    ( (Response == yes ; Response == y)
      ->
       assert(yes(Question)) ;
       assert(no(Question)), fail).

:- dynamic yes/1,no/1.

/* How to verify something */
verify(S) :- (yes(S) -> true ;
               (no(S)  -> fail ;
               ask(S))).

/* undo all yes/no assertions */
undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.