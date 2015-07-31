# CSC320-SATSolver
CSC320 sudoku solver. (SAT Solver)

##Members:
Brett Binnersley, V00776751
Brett Blashko, V00759982
Deepak Parmar, V00770095


##Description:
SAT solver for Sudoku puzzles.

Please refer SAT-Report.txt for more details.

This program is a sudoku solver that will transform a sudoku puzzle (9x9) into an
instance of the NP-complete SAT problem.  It will read a sudoku puzzle table and
convert it to a set of boolean formulae (used by SAT solvers) to solve the puzzle.

##Instructions:

1) Download the SudokuSolver.zip file

2) After extraction, run the following command (assuming minisat is installed on the machine):

	python main.py input.txt minisat
	
##Contents:

The submission includes the following files:

	main.py 

The main.py program will read in the input file and encode it into a string. This main file also includes code to generate the minimal number of clauses by writing it to a tempOutput.txt file after running each of the functions included in the second file (methodCNF.py).  This encoding is minimal.
	
	methodCNF.py 

The methodCNF.py includes the following functions:
	
generateRowCNF:  generate the # rows 

generateColumnCNF:   generate the # columns

generate3x3CNF:   generate the 3x3 CNF grid

generatePrefilledCNF:  generate the prefilled CNF cells

generateIndivCNF:   generate the individual CNF cells
