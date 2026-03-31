% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

% Add initial state facts
sudoku(X,Y,N) :- initial(X,Y,N).

% Generator: exactly one number per cell
1 { sudoku(X,Y,N) : N=1..9 } 1 :- X=1..9, Y=1..9.

% Each number appears exactly once per row
:- sudoku(X,Y,N), sudoku(X,Y',N), Y != Y'.

% Each number appears exactly once per column
:- sudoku(X,Y,N), sudoku(X',Y,N), X != X'.

% Each number appears exactly once per 3x3 subgrid
:- sudoku(X,Y,N), sudoku(X',Y',N), (X,Y) != (X',Y'), ((X-1)/3) == ((X'-1)/3), ((Y-1)/3) == ((Y'-1)/3).

#show sudoku/3.
