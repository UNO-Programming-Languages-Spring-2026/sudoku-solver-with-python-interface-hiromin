% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
% Add initial state
sudoku(X,Y,N) :- initial(X,Y,N).

% Generator: exactly one number per cell
1 { sudoku(X,Y,N) : N=1..9 } 1 :- X=1..9, Y=1..9.

% Each number appears exactly once per row
:- X=1..9, N=1..9,
   #count { Y : sudoku(X,Y,N) } != 1.

% Each number appears exactly once per column
:- Y=1..9, N=1..9,
   #count { X : sudoku(X,Y,N) } != 1.

% Assign each a subgrid
subgrid(X, Y, ((((X-1)/3)*3 + ((Y-1)/3))+1)) :- sudoku(X, Y, _).

% Each number appears exactly once per subgrid
% :- X=1..4, Y=1..4,
%     #count { G  : sudoku(X, Y, N), subgrid(X, Y, G) } != 1.
:- sudoku(X, Y, N), sudoku(X', Y', N), (X,Y) != (X',Y'),
(( (X-1)/3)*3 + (Y-1)/3) = (( (X'-1)/3)*3 + (Y'-1)/3).


#show sudoku/3.
