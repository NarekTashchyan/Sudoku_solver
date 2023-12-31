#importing pprint library beacause we want it to print like a sudoku board
from pprint import pprint
#writing a function to detect empty spots 
def empty_spot(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==0:
                return r, c
            
    return None, None
#writing a funcion to see if a random number from 1-9 is legal for the spot or not
def is_valid(puzzle,guess,row,col):
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals  :
        return False
    
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True
#now combining the functions         
def solve_sudoku(puzzle):
    row, col =empty_spot(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        
        if is_valid(puzzle,guess,row,col):

            puzzle[row][col]=guess

            if solve_sudoku(puzzle):
                return True
            
        puzzle[row][col]=0
    
    return False

if __name__=="__main__":
    board = [
            [0,3,4,0,0,8,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,8,0,0,1,9,0,0,5],
            [0,4,0,0,8,6,0,7,9]]
    
    print(solve_sudoku(board))
    pprint(board)
