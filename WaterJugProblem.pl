% Declaring condition for final state
start(2,0):-write(' 4 liter Jug:   2 | 3 liter Jug:   0|\n'),
            write('Problem Solved!\n').      

% Starting from the initial state and take rules as input from the user
start(A,B):-write(' 4 liter Jug:   '),write(A),write('| 3 liter Jug:   '),
            write(B),write('|\n'),
            write(' Enter Rule::'),
            read(N),
            contains(A,B,N).

% Rule logic
contains(_,B,1):-start(4,B).
contains(A,_,2):-start(A,3).
contains(_,B,3):-start(0,B).
contains(A,_,4):-start(A,0).
contains(A,B,5):-N is B-4+A, start(4,N).
contains(A,B,6):-N is A-3+B, start(N,3).
contains(A,B,7):-N is A+B, start(N,0).
contains(A,B,8):-N is A+B, start(0,N).

% Main function to implement the problem and display instructions
waterjug(A,B):-write('WATER JUG PROBLEM'),nl,nl,
        write('Follow the Rules: '),nl,
        write('Rule 1: Fill 4 liter Jug\n'),nl,
        write('Rule 2: Fill 3 liter Jug\n'),nl,
        write('Rule 3: Empty 4 liter Jug\n'),nl,
        write('Rule 4: Empty 3 liter Jug\n'),nl,
        write('Rule 5: Fill 4 liter Jug with 3 liter Jug\n'),nl,
        write('Rule 6: Fill 3 liter Jug with 4 liter Jug\n'),nl,
        write('Rule 7: Empty 3 liter Jug into 4 liter Jug\n'),nl,
        write('Rule 8: Empty 4 liter Jug into 3 liter Jug\n'),nl,nl,
        write(' 4 liter Jug:   0 | 3 liter Jug:   0'),nl,
        write(' Enter Rule::'),
        read(N),nl,
        contains(0,0,N).