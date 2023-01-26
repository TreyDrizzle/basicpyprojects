from pprint import pprint



def find_next_empty(puzzle):
    # Finds the next row, col on the puxxle that's not filled yet ----> rep with -1
    # Return row,col tuple (or (None, None) if there is none)

    # Using 0-8 for our indices
    for r in range(9):
        for c in range(9): #range(9) is 0,1,2, .... 8
            if puzzle[r][c] == -1:
                return r,c 
        
    
    return None, None # if no spaces in puzzle are empty (-1)

def is_vaild(puzzle, guess, row, col):
    # Figures out whether the guess at the row/col of the puzzle is a valid guess
    # Returns True if is valid, false otherwise

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Square matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start +3):
            if puzzle[r][c] == guess:
                return False

    # If all cases pass return True
    return True

def solve_sudoku(puzzle):
    # Solve sudoku using Backtracking
    # Our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # Return whether a solution exists 
    # mutates puzzle to be the solution (if solution exists)

    # Step 1: Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there is nowhere left, then we're done beacuse we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1,2,3, ...9
        # step 3: Check if this a vaild guess
        if is_vaild(puzzle, guess, row, col):
            # Step 3.1 If this guess is valid place guess in puzzle
            puzzle[row][col] = guess
            # Recurse this puzzle
            # Step 4 Recursively call our fuction 
            if solve_sudoku(puzzle):
                return True

        # Step 5 if not vaild OR if our guess does not solve the puzzle, then we need to backtrack and try and new number 
        puzzle[row][col] = -1 # Reset Guess

    
    # Step 6 if none of the numbers work then this puzzle is unsolveable. 
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)