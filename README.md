# MyPythonRepos
Contains my Python projects.

This ropository records the three solutions to the Sudoku game.
1. numpy_sqlite: My first but least efficient way. 
  Use Sqlite database and numpy package to accelerate enumeration of possible permutations.
  Then use Query statements to fetch data and filter the rows until find the final answer.
  
2. backtracking: Also use numpy, and a helper array to keep track of position on the board. 
   Everytime add 1 to current position and check its validity and use backtracking to modify previous numbers.
   
3. recursion: To base case of this recursion is when no empty (or 0) is found on the board.
  Find the next empty (or 0) postion of the board and iterate through the valid numbers in range 1-10 to see if there is a way to solve the board.
  If not, set it to empty(or 0) back.
