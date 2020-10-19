male(ross).
female(monica).

friends(ross, chandler).
friends(rachel, monica).
friends(rachel, chandler).
friends(A, B):- friends(B, A).

loves(chandler, monica).
loves(ross, rachel).
loves(X, Y):- loves(Y, X).

siblings(ross, monica).
brother(P, Q):- siblings(P, Q),male(P).
sister(Q, P):- siblings(P, Q),female(Q).